"""
Terms:
- busday: normal work day (usually Mo to Fr)
- weekend: off days each week (usually Sa and So)
- offday: holiday or weekend
- onday: work day which is not a holiday
"""

from typing import NamedTuple

import pandas as pd
import nilmtk

from enilm.dt import (
    get_busdays_filter_for_datetime_index,
    get_weekends_filter_for_datetime_index,
    get_holidays_filter_for_datetime_index,
)
from enilm.checkers import check_valid_pd_series_type, PDSerTypes
from enilm.etypes import DatasetID
from enilm.nilmdt import get_holidays_calendar_from_ds


def split_np_busday_weekend():
    raise NotImplementedError


class PDBudsdayWeekendSplitResult(NamedTuple):
    busdays: pd.Series
    weekends: pd.Series


def split_pd_busday_weekend(ser: pd.Series) -> PDBudsdayWeekendSplitResult:
    """
    df: dataframe with index of type pd.DatetimeIndex and float values
    """
    assert check_valid_pd_series_type(ser, PDSerTypes.PDTimeSeries)

    filt = get_busdays_filter_for_datetime_index(ser.index)

    return PDBudsdayWeekendSplitResult(
        busdays=ser[filt],
        weekends=ser[~filt],
    )


class PDOnOffdaySplitResult(NamedTuple):
    ondays: pd.Series
    offdays: pd.Series


def split_pd_on_offday(ser: pd.Series, ds: DatasetID) -> PDOnOffdaySplitResult:
    """
    offday is either a weekend or a holiday
    ondays are the rest

    df: dataframe with index of type pd.DatetimeIndex and float values
    """
    assert check_valid_pd_series_type(ser, PDSerTypes.PDTimeSeries)

    weekends_filt = get_weekends_filter_for_datetime_index(ser.index)
    holidays_filt = get_holidays_filter_for_datetime_index(
        ser.index, get_holidays_calendar_from_ds(ds)
    )

    return PDOnOffdaySplitResult(
        ondays=ser[~(weekends_filt | holidays_filt)],
        offdays=ser[weekends_filt | holidays_filt],
    )
