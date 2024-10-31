# save and load pandas series
from enum import Enum
from pathlib import Path

import pandas as pd


class PandasSeriesStoreFormat(Enum):
    FEATHER = "feather"
    HDF5 = "hdf5"
    PICKLE = "pickle"
    CSV = "csv"


def save(ser: pd.Series, ser_path: Path, store_format: PandasSeriesStoreFormat = PandasSeriesStoreFormat.HDF5):
    if not ser_path.parent.exists():
        ser_path.parent.mkdir(parents=True, exist_ok=True)
    
    if store_format is PandasSeriesStoreFormat.HDF5:
        assert ser_path.suffix == ".h5"
        ser_path.parent.mkdir(parents=True, exist_ok=True)
        ser.to_hdf(ser_path, key="ser", mode="w")
    else:
        raise NotImplementedError()


def load(ser_path: Path, store_format: PandasSeriesStoreFormat = PandasSeriesStoreFormat.HDF5) -> pd.Series:
    if store_format is PandasSeriesStoreFormat.HDF5:
        assert ser_path.suffix == ".h5"
        return pd.read_hdf(ser_path)
    else:
        raise NotImplementedError()


def compute_or_load(fn, fn_params, ser_path: Path, store_format: PandasSeriesStoreFormat = PandasSeriesStoreFormat.HDF5) -> pd.Series:
    if ser_path.exists():
        return load(ser_path, store_format)

    ser_result = fn(**fn_params)
    save(ser_result, ser_path, store_format)
    return ser_result
