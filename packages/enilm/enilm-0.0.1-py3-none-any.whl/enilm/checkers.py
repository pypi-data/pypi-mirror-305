"""Sanity checks"""

from enum import Enum

import numpy as np
import pandas as pd
from nilmtk import TimeFrame


def check_timeframe(timeframe: TimeFrame):
    timeframe.check_tz()


def check_valid_date(year: int, month: int, day: int):
    raise NotImplementedError


class ArrTypes(Enum):
    SamplesF64: str = "SamplesF64"
    ChunksSamplesF64: str = "ChunksSamplesF64"
    PDTimestamps: str = "PDTimestamps"
    NPTimestamps: str = "NPTimestamps"
    NPBool: str = "NPBool"


def check_vaild_arr_type(arr: np.ndarray, arr_type: ArrTypes) -> bool:
    if arr_type == ArrTypes.SamplesF64:
        return isinstance(arr[0], np.float64)

    if arr_type == ArrTypes.ChunksSamplesF64:
        return len(arr.shape) == 2 and isinstance(arr[0][0], np.float64)

    if arr_type == ArrTypes.PDTimestamps:
        return isinstance(arr[0], pd.Timestamp)

    if arr_type == ArrTypes.NPTimestamps:
        return isinstance(arr[0], np.datetime64)

    if arr_type == ArrTypes.NPBool:
        return arr.dtype == bool


class PDSerTypes(Enum):
    PDTimeSeries: str = "PDTimeSeries"


def check_valid_pd_series_type(ser: pd.Series, ser_type: PDSerTypes) -> bool:
    if ser_type == PDSerTypes.PDTimeSeries:
        if not hasattr(ser, "index"):
            return False
        return isinstance(ser.index, pd.DatetimeIndex) and (ser.dtype == np.float32 or ser.dtype == np.float64 or ser.dtype == np.int64)
