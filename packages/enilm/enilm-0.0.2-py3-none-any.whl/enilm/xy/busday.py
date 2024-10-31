from typing import Tuple

import enilm


def split_busday_weekend(
    xy: enilm.etypes.xy.XYArray,
    times: enilm.etypes.xy.XYNPTimesArray,
    np_is_busday_kwargs={},
) -> Tuple[
    enilm.etypes.xy.XYArray,  # for busday
    enilm.etypes.xy.XYArray,  # for weekends
]:
    """
    np_is_busday_kwargs passed to np.is_busday
    """
    assert list(times.y.keys()) == list(xy.y.keys())

    x_filt = enilm.dt.get_busdays_filter_with_np_is_busday(times.x, np_is_busday_kwargs)
    y_filt = {}
    for app_name in xy.y.keys():
        y_filt[app_name] = enilm.dt.get_busdays_filter_with_np_is_busday(
            times.y[app_name], np_is_busday_kwargs
        )

    xy_busday = enilm.etypes.xy.XYArray(
        x=xy.x[x_filt],
        y={app_name: xy.y[app_name][y_filt[app_name]] for app_name in xy.y.keys()},
    )
    xy_weekends = enilm.etypes.xy.XYArray(
        x=xy.x[~x_filt],
        y={app_name: xy.y[app_name][~y_filt[app_name]] for app_name in xy.y.keys()},
    )

    assert len(xy_busday.x) + len(xy_weekends.x) == len(xy.x)
    # assert len(xy_busday.y) + len(xy_weekends.y) == len(xy.y)

    return xy_busday, xy_weekends
