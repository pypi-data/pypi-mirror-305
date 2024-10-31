# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import logging
import os
import pickle

import numpy as np
import torch
from ai_models_gfs.model import Model
from aurora import Batch
from aurora import Metadata
from aurora import rollout
from aurora.model.aurora import Aurora
from aurora.model.aurora import AuroraHighRes
from netCDF4 import Dataset as DS
import datetime
LOG = logging.getLogger(__name__)


class AuroraModel(Model):

    download_url = "https://huggingface.co/microsoft/aurora/resolve/main/{file}"

    # Input
    area = [90, 0, -90, 360 - 0.25]
    grid = [0.25, 0.25]

    surf_vars = ("2t", "10u", "10v", "msl")
    atmos_vars = ("z", "u", "v", "t", "q")
    levels = (1000, 925, 850, 700, 600, 500, 400, 300, 250, 200, 150, 100, 50)

    lagged = (-6, 0)

    #  For the MARS requets
    param_sfc = surf_vars
    param_level_pl = (atmos_vars, levels)

    # Output

    expver = "auro"
    lora = None

    def run(self):

        # TODO: control location of cache

        use_lora = self.lora if self.lora is not None else self.use_lora

        LOG.info(f"Model is {self.__class__.__name__}, use_lora={use_lora}")

        model = self.klass(use_lora=use_lora)
        model = model.to(self.device)

        path = os.path.join(self.assets, os.path.basename(self.checkpoint))
        if os.path.exists(path):
            LOG.info("Loading Aurora model from %s", path)
            model.load_checkpoint_local(path, strict=False)
        else:
            LOG.info("Downloading Aurora model %s", self.checkpoint)
            try:
                model.load_checkpoint("microsoft/aurora", self.checkpoint, strict=False)
            except Exception:
                LOG.error("Did not find a local copy at %s", path)
                raise

        LOG.info("Loading Aurora model to device %s", self.device)

        model = model.to(self.device)
        model.eval()

        fields_pl = self.fields_pl
        fields_sfc = self.fields_sfc

        Nj, Ni = fields_pl[0].shape

        to_numpy_kwargs = dict(dtype=np.float32)

        #Dictionary to hold output and variable mappings
        if 'n' in self.nc_or_grib:
            out,mapping,varmap = initialize_nc_dict(self.lead_time,6)

        templates = {}

        # Shape (Batch, Time, Lat, Lon)
        surf_vars = {}

        for k in self.surf_vars:
            f = fields_sfc.sel(param=k).order_by(valid_datetime="ascending")
            templates[k] = f[-1]
            f = f.to_numpy(**to_numpy_kwargs)
            if 'n' in self.nc_or_grib:
                out[varmap[k]]['values'][0] = f[-1]
            f = torch.from_numpy(f)
            f = f.unsqueeze(0)  # Add batch dimension
            surf_vars[k] = f

        # Shape (Lat, Lon)
        static_vars = {}
        with open(os.path.join(self.assets, self.download_files[0]), "rb") as f:
            static_vars = pickle.load(f)
            for k, v in static_vars.items():
                static_vars[k] = torch.from_numpy(v)

        # Shape (Batch, Time, Level, Lat, Lon)


        atmos_vars = {}
        for k in self.atmos_vars:
            f = fields_pl.sel(param=k).order_by(valid_datetime="ascending", level=self.levels)
            for level_idx,level in enumerate(self.levels):
                templates[(k, level)] = f.sel(level=level)[-1]
                if 'n' in self.nc_or_grib:
                    ftemp = f.sel(level=level)[-1].to_numpy(**to_numpy_kwargs)
                    out[varmap[k]]['values'][0, level_idx] = ftemp
            f = f.to_numpy(**to_numpy_kwargs).reshape(len(self.lagged), len(self.levels), Nj, Ni)

            f = torch.from_numpy(f)
            f = f.unsqueeze(0)  # Add batch dimension
            atmos_vars[k] = f
        if 'g' in self.nc_or_grib:
            self.write_input_fields(fields_pl + fields_sfc)

        # https://microsoft.github.io/aurora/batch.html

        N, W, S, E = self.area
        batch = Batch(
            surf_vars=surf_vars,
            static_vars=static_vars,
            atmos_vars=atmos_vars,
            metadata=Metadata(
                lat=torch.linspace(N, S, Nj),
                lon=torch.linspace(W, E, Ni),
                time=(self.start_datetime,),
                atmos_levels=self.levels,
            ),
        )

        assert len(batch.metadata.lat) == Nj
        assert len(batch.metadata.lon) == Ni
        LOG.info("Starting inference")
        with torch.inference_mode():

            with self.stepper(6) as stepper:
                for i, pred in enumerate(rollout(model, batch, steps=self.lead_time // 6)):
                    step = (i + 1) * 6

                    for k, v in pred.surf_vars.items():
                        data = np.squeeze(v.cpu().numpy())
                        data = self.nan_extend(data)
                        assert data.shape == (Nj, Ni)
                        if 'n' in self.nc_or_grib:
                            out[varmap[k]]['values'][i+1] = data
                        if 'g' in self.nc_or_grib:
                            self.write(data, template=templates[k], step=step, check_nans=True)

                    for k, v in pred.atmos_vars.items():
                        v = v.cpu().numpy()
                        for j, level in enumerate(self.levels):
                            data = np.squeeze(v[:, :, j])
                            data = self.nan_extend(data)
                            assert data.shape == (Nj, Ni)
                            if 'n' in self.nc_or_grib:
                                out[varmap[k]]['values'][i+1, j] = data
                            if 'g' in self.nc_or_grib:
                                self.write(data, template=templates[(k, level)], step=step, check_nans=True)
                    stepper(i, step)

        #Write nc
        if 'n' in self.nc_or_grib:
            write_nc(out,self.lead_time,6,self.date,self.time,self.ncpath)

    def nan_extend(self, data):
        return np.concatenate(
            (data, np.full_like(data[[-1], :], np.nan, dtype=data.dtype)),
            axis=0,
        )

    def parse_model_args(self, args):
        import argparse

        parser = argparse.ArgumentParser("ai-models aurora")

        parser.add_argument(
            "--lora",
            type=lambda x: (str(x).lower() in ["true", "1", "yes"]),
            nargs="?",
            const=True,
            default=None,
            help="Use LoRA model (true/false). Default depends on the model.",
        )

        return parser.parse_args(args)


class Aurora0p25(AuroraModel):
    expver = "au25"

    klass = Aurora
    download_files = ("aurora-0.25-static.pickle",)
    # Input
    area = [90, 0, -90, 360 - 0.25]
    grid = [0.25, 0.25]


# https://microsoft.github.io/aurora/models.html#aurora-0-25-pretrained
class Aurora0p25Pretrained(Aurora0p25):
    use_lora = False
    checkpoint = "aurora-0.25-pretrained.ckpt"


# https://microsoft.github.io/aurora/models.html#aurora-0-25-fine-tuned
class Aurora0p25FineTuned(Aurora0p25):
    use_lora = True
    checkpoint = "aurora-0.25-finetuned.ckpt"

    # We want FC, step=0
    def patch_retrieve_request(self, r):
        if r.get("class", "od") != "od":
            return

        if r.get("type", "an") not in ("an", "fc"):
            return

        if r.get("stream", "oper") not in ("oper", "scda"):
            return

        r["type"] = "fc"

        time = r.get("time", 12)

        r["stream"] = {
            0: "oper",
            6: "scda",
            12: "oper",
            18: "scda",
        }[time]


# https://microsoft.github.io/aurora/models.html#aurora-0-1-fine-tuned
class Aurora0p1FineTuned(AuroraModel):
    download_files = ("aurora-0.1-static.pickle",)
    # Input
    area = [90, 0, -90, 360 - 0.1]
    grid = [0.1, 0.1]

    klass = AuroraHighRes
    use_lora = True
    checkpoint = "aurora-0.1-finetuned.ckpt"


# model = Aurora0p1FineTuned


def model(model_version, **kwargs):

    # select with --model-version

    models = {
        "0.25-pretrained": Aurora0p25Pretrained,
        "0.25-finetuned": Aurora0p25FineTuned,
        "0.1-finetuned": Aurora0p1FineTuned,
        "default": Aurora0p1FineTuned,
        "latest": Aurora0p1FineTuned,  # Backward compatibility
    }

    if model_version not in models:
        LOG.error(f"Model version {model_version} not found, using default")
        LOG.error(f"Available models: {list(models.keys())}")
        raise ValueError(f"Model version {model_version} not found")

    return models[model_version](**kwargs)

def initialize_nc_dict(lead_time,hour_steps):
    out = {
        'u10': {
            'values': np.zeros((lead_time // hour_steps + 1, 721, 1440)),
            'name': '10 metre U wind component', 'units': 'm s-1'
        },
        'v10': {
            'values': np.zeros((lead_time // hour_steps + 1, 721, 1440)),
            'name': '10 metre V wind component', 'units': 'm s-1'
        },
        't2': {
            'values': np.zeros((lead_time // hour_steps + 1, 721, 1440)),
            'name': '2 metre temperature', 'units': 'K'
        },
        'msl': {
            'values': np.zeros((lead_time // hour_steps + 1, 721, 1440)),
            'name': 'Pressure reduced to MSL', 'units': 'Pa'
        },
        't': {
            'values': np.zeros((lead_time // hour_steps + 1, 13, 721, 1440)),
            'name': 'Temperature', 'units': 'K'
        },
        'u': {
            'values': np.zeros((lead_time // hour_steps + 1, 13, 721, 1440)),
            'name': 'U component of wind', 'units': 'm s-1'
        },
        'v': {
            'values': np.zeros((lead_time // hour_steps + 1, 13, 721, 1440)),
            'name': 'V component of wind', 'units': 'm s-1'
        },
        'z': {
            'values': np.zeros((lead_time // hour_steps + 1, 13, 721, 1440)),
            'name': 'Geopotential', 'units': 'm2 s-2'
        },
        'q': {
            'values': np.zeros((lead_time // hour_steps + 1, 13, 721, 1440)),
            'name': 'Specific humidity', 'units': 'kg kg-1'
        },
    }

    mapping = {
        50:12,
        100:11,
        150:10,
        200:9,
        250:8,
        300:7,
        400:6,
        500:5,
        600:4,
        700:3,
        850:2,
        925:1,
        1000:0
    }

    varmap = {
        "u":"u",
        "v":"v",
        "z":"z",
        "t":"t",
        "q":"q",
        "10u":"u10",
        "10v":"v10",
        "msl":"msl",
        "2t":"t2"
    }


    return out,mapping,varmap

def create_variable(f, name, dimensions, data, attrs):
    if name in ['time','level']:
        dtype = 'i4'
    else:
        dtype = 'f4'
    var = f.createVariable(name, dtype, dimensions,compression='zlib',complevel=4)
    var[:] = data
    for attr_name, attr_value in attrs.items():
        var.setncattr(attr_name, attr_value)

def write_nc(out,lead_time,hour_steps,date,time,path):
    outdir = path
    f = DS(outdir, 'w', format='NETCDF4')
    f.createDimension('time', lead_time // hour_steps + 1)
    f.createDimension('level', 13)
    f.createDimension('longitude', 1440)
    f.createDimension('latitude', 721)

    year = str(date)[0:4]
    month = str(date)[4:6]
    day = str(date)[6:8]
    hh = str(int(time/100)).zfill(2)
    initdt = datetime.datetime.strptime(f"{year}{month}{day}{hh}","%Y%m%d%H")
    inityr = str(initdt.year)
    initmnth = str(initdt.month).zfill(2)
    initday = str(initdt.day).zfill(2)
    inithr = str(initdt.hour).zfill(2)
    times = []
    for i in np.arange(0,lead_time + hour_steps,hour_steps):
        times.append(int((initdt + datetime.timedelta(hours=int(i))).timestamp()))

    # Create time, longitude, latitude, and level variables in the NetCDF file
    create_variable(
        f, 'time', ('time',), np.array(times), {
            'long_name': 'Date and Time', 'units': 'seconds since 1970-1-1',
            'calendar': 'standard'
        }
    )
    create_variable(
        f, 'longitude', ('longitude',), np.arange(0, 360, 0.25), {
            'long_name': 'Longitude', 'units': 'degree'
        }
    )
    create_variable(
        f, 'latitude', ('latitude',), np.arange(-90, 90.25, 0.25)[::-1], {
            'long_name': 'Latitude', 'units': 'degree'
        }
    )
    create_variable(
        f, 'level', ('level',), np.array(
            [50, 100, 150, 200, 250, 300, 400, 500, 600, 700, 850, 925, 1000]
        )[::-1], {'long_name': 'Isobaric surfaces', 'units': 'hPa'}
    )
    # Create variables for each meteorological parameter
    for variable in [
        'u10', 'v10', 't2', 'msl', 't', 'u', 'v', 'z', 'q'
    ]:
        dims = ('time', 'level', 'latitude', 'longitude') if variable in [
            'u', 'v', 'z', 't', 'q'
        ] else ('time', 'latitude', 'longitude')
        create_variable(
            f, variable, dims, out[variable]['values'], {
                'long_name': out[variable]['name'], 'units': out[variable]['units']
            }
        )

    f.Conventions = 'CF-1.8'
    f.model_name = 'Aurora'
    f.model_version = 'v1'
    f.initialization_model = 'GFS'
    f.initialization_time = '%s-%s-%sT%s:00:00' % (inityr,initmnth,initday,inithr)
    f.first_forecast_hour = str(0)
    f.last_forecast_hour = str(lead_time)
    f.forecast_hour_step = str((lead_time // 6)+1)
    f.creation_time = (datetime.datetime.utcnow()).strftime('%Y-%m-%dT%H:%M:%S')
    f.close()
