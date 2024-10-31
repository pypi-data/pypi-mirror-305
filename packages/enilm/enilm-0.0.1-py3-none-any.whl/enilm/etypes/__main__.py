from enum import Enum, auto
from typing import Union, NamedTuple

from pydantic import PositiveInt


class ParamsCount(NamedTuple):
    count: int
    total: int


AppName = str
HouseNr = PositiveInt

class Datasets(Enum):
    """Enum of NILMTK supported and tested data sets, see `nilmtk.dataset_converters`"""
    DRED = auto()
    REDD = auto()
    BLOND = auto()
    REFIT = auto()
    SMART = auto()
    UKDALE = auto()
    SynD = auto()
    ECO = auto()
    HIPE = auto()
    HIPE_WEEK = auto()
    AMP = auto()
    DEDDIAG = auto()
    ENERTALK = auto()


DatasetID = Union[Datasets, str]
