from typing import NamedTuple, Dict, TypedDict

import pandas as pd

from .__main__ import AppName
from .arr import *


class XYSeries(NamedTuple):
    x: pd.Series
    y: Dict[AppName, pd.Series]


class XYArray(NamedTuple):
    x: SamplesF64
    y: Dict[AppName, SamplesF64]


class XYChunksArray(NamedTuple):
    x: ChunksSamplesF64
    y: Dict[AppName, ChunksSamplesF64]


class XYPDTimesArray(NamedTuple):
    x: PDTimestamps
    y: Dict[AppName, PDTimestamps]


class XYNPTimesArray(NamedTuple):
    x: NPTimestamps
    y: Dict[AppName, NPTimestamps]


class TrainTestXYArray(NamedTuple):
    train: XYArray
    test: XYArray


class TimesTrainTestNPXYArray(NamedTuple):
    train: XYNPTimesArray
    test: XYNPTimesArray


class TimesTrainTestPDXYArray(NamedTuple):
    train: XYPDTimesArray
    test: XYPDTimesArray


class XYNormParams(NamedTuple):
    x_mean: float
    x_std: float
    y_mean: Dict[AppName, float]
    y_std: Dict[AppName, float]


class XYNormParamsDict(TypedDict):
    x_mean: float
    x_std: float
    y_mean: Dict[AppName, float]
    y_std: Dict[AppName, float]
