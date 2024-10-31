"""Common plotting function with plotly"""
from typing import Callable, Optional, Union, Iterable
from pathlib import Path

from nilmtk import ElecMeter, Appliance, MeterGroup
from nilmtk.electric import Electric
from plotly import graph_objects as go
import tensorflow as tf

from enilm.activations import get_appliance_activations
from enilm.appliances import get_elec
import enilm.etypes.arr
import enilm.etypes.xy


def _create_scatter_added(fig: go.Figure, webgl: bool):
    def fn(**plt_kwargs):
        if webgl:
            fig.add_trace(go.Scattergl(**plt_kwargs))
        else:
            fig.add_trace(go.Scatter(**plt_kwargs))

    return fn


def plot_sample(
    win_size: int,
    x: enilm.etypes.arr.SamplesF64,
    y: enilm.etypes.arr.SamplesF64,
    app_name: enilm.etypes.xy.AppName,
    # for pred
    x_chunks: Optional[enilm.etypes.arr.ChunksSamplesF64] = None,
    denorm: Optional[Callable] = None,
    model: Optional[tf.keras.Model] = None,
    # webgl
    webgl: bool = True,
    # range selection
    plot_slice: Optional[slice] = None,
) -> go.Figure:
    """
    If with pred then model, x_chunks, and denorm must be proveded
    """
    if plot_slice:
        x = x[plot_slice]
        y = y[plot_slice]
        if x_chunks is not None:
            x_chunks = x_chunks[plot_slice]

    fig = go.Figure()
    trace_adder = _create_scatter_added(fig, webgl)

    n = 10 * win_size

    dx = x[win_size // 2 : n]
    trace_adder(y=dx, name="mains (x)")

    dy = y[win_size // 2 : n]
    fig.add_scattergl(y=dy, name=f"{app_name} (y)")

    if model:
        pred = model(x_chunks[:n]).numpy().flatten()
        fig.add_scattergl(y=denorm(pred), name=f"pred: {app_name}")

    return fig


def plot_elec(elec: Union[Electric, Iterable[Electric]], webgl: bool = True, **kwargs) -> go.Figure:
    """
    Plot for each appliance/elec meter a trace. If a meter group is based, the mains is plotted too.

    Parameters
    ----------
    elec: a single `MeterGroup`, a single `ElecMeter` or an iterable of `ElecMeter`
    webgl: use webgl to render scatter traces (see https://plotly.com/python/webgl-vs-svg/)
    kwargs: passed to load function

    Returns
    -------
    A plotly figure
    """
    fig: go.Figure = go.Figure()
    trace_adder = _create_scatter_added(fig, webgl)

    def get_data(e: Electric):
        g = e.load(**kwargs)
        data = next(g)
        if len(data.columns) > 1:
            # maybe multiple power types
            print("Warning: Loaded power data has multiple columns, using active power")
            data = data["power"]["active"]
        data = data.squeeze()  # to convert to series, since it has one column
        assert next(g, None) is None, "Not all data can be loaded at once to memory"
        return data

    def add_elecmeter(e: ElecMeter):
        if e.is_site_meter():
            data = get_data(e)
            trace_adder(x=data.index, y=data, name="Mains")
        else:
            assert len(e.appliances) == 1
            app: Appliance = e.appliances[0]
            data = get_data(e)
            trace_adder(x=data.index, y=data, name=app.label(True))

    if isinstance(elec, MeterGroup):
        # aggregated (by nilmtk) from all sub-meters
        data = get_data(elec)
        trace_adder(x=data.index, y=data, name="Aggregated")

        # mains
        mains_elec = elec.mains()
        data = get_data(mains_elec)
        trace_adder(x=data.index, y=data, name="Mains")

        # appliances
        for app in elec.appliances:
            app_elec = get_elec(app, elec)
            data = get_data(app_elec)
            trace_adder(x=data.index, y=data, name=app.label(True))

    elif isinstance(elec, ElecMeter):
        add_elecmeter(elec)

    elif isinstance(elec, Iterable):
        for e in elec:
            assert isinstance(e, ElecMeter)
            add_elecmeter(e)

    return fig


def plot_activations(elec: Union[Electric, Iterable[Electric]], webgl: bool = True, **kwargs):
    """
    Plot the trace of each elec meter in the provided elec as `common.plot.plot_elec`, additionally overlap
     each trace with the activations for that appliance as reported by
     `common.activations.get_appliance_activations`

    Parameters
    ----------
    elec: a single `MeterGroup`, a single `ElecMeter` or an iterable of `ElecMeter`
    webgl: use webgl to render scatter traces (see https://plotly.com/python/webgl-vs-svg/)
    kwargs: passed to nilmtk.electric.Electric.load
        e.g. sections=[TimeFrame(start, stop), ...], ...

    Returns
    -------
    A plotly figure
    """
    fig = plot_elec(elec, **kwargs)
    trace_adder = _create_scatter_added(fig, webgl)

    def add_trace(trace, name):
        trace_adder(
            x=trace.index,
            y=trace,
            line=dict(color="firebrick"),
            mode="lines",
            name=name,
        )

    if isinstance(elec, ElecMeter):
        for i, trace in enumerate(get_appliance_activations(elec, **kwargs)):
            add_trace(trace, f"activation {i + 1}")
    elif isinstance(elec, Iterable):
        for e in elec:
            assert isinstance(e, ElecMeter)
            assert len(e.appliances) == 1
            app = e.appliances[0]
            for i, trace in enumerate(get_appliance_activations(e, **kwargs)):
                add_trace(trace, f"{app.label(True)} activation {i + 1}")
    elif isinstance(elec, MeterGroup):
        for app in elec.appliances:
            app_elec = get_elec(app, elec)
            for i, trace in enumerate(get_appliance_activations(app_elec, **kwargs)):
                add_trace(trace, f"{app.label(True)} activation {i + 1}")

    return fig


def save_html(fig: go.Figure, path: Path):
    """
    Save the plotly figure as html file

    Parameters
    ----------
    fig: the figure to save
    path: the path to save to
    """
    if not path.parent.exists():
        path.parent.mkdir(parents=True)
    fig.write_html(str(path))


if __name__ == "__main__":
    import datetime
    from nilmtk import TimeFrame
    import enilm

    loaded = enilm.datasets.loaders.load(enilm.etypes.Datasets.REFIT, building_nr=3)
    plot_elec(
        loaded.elec,
        sections=[
            TimeFrame(
                start=datetime.datetime(year=2014, month=4, day=2),
                end=datetime.datetime(year=2014, month=4, day=3),
                tz=loaded.tz,
            )
        ],
        sample_period=120,
    )
