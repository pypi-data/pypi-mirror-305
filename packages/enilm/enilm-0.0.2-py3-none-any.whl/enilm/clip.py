from typing import Union

import pandas as pd
from nilmtk import DataSet

from enilm.checkers import check_valid_pd_series_type, PDSerTypes
from enilm.nilmdt import get_tzinfo_from_ds
from enilm.etypes import Datasets


def to_day_start(ser: pd.Series, ds: Union[DataSet, Datasets]) -> pd.Series:
    assert check_valid_pd_series_type(ser, PDSerTypes.PDTimeSeries)

    first_index = ser.index[0]
    first_day = pd.Timestamp(
        year=first_index.year,
        month=first_index.month,
        day=first_index.day,
        tz=get_tzinfo_from_ds(ds),
    )

    # is first sample at exactly the start of the day? => no need for clipping
    if ser.index[0] == first_day:
        return ser
    else:
        first_full_day = first_day + pd.Timedelta(days=1)
        # TODO: find first date where date >= first_full_day
        raise NotImplementedError
