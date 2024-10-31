from dataclasses import dataclass
from typing import Callable, Optional
from pathlib import Path

import tensorflow as tf
import pandas as pd
import plotly.express as px

import enilm
from .section import Section


@dataclass
class LoadTrainParams:
    config: enilm.config.ExpConfig
    app_name: enilm.etypes.AppName
    base_model: tf.keras.Model
    denorm: Callable[[float], enilm.etypes.arr.SamplesF64]
    train_chunks: enilm.etypes.xy.XYChunksArray
    test_chunks: enilm.etypes.xy.XYChunksArray
    test: enilm.etypes.xy.XYArray
    model_path_base: Optional[Path] = None
    plot_slice: Optional[slice] = None
    generate_plots: bool = True
    save_checkpoint: bool = False


def load_train(
    p: LoadTrainParams,
) -> enilm.models.utils.train.TrainTestResult:
    if p.model_path_base is None:
        p.model_path_base = Path(
            "models"
        ) / enilm.models.utils.paths.create_model_path_base(p.config)

    if not p.model_path_base.exists():
        res = enilm.models.utils.train.train_test(
            p.model_path_base,
            params=enilm.models.utils.train.TrainTestParams(
                model=p.base_model,
                x_chunks=p.train_chunks.x,
                y_chunks=p.train_chunks.y[p.app_name],
                test_x_chunks=p.test_chunks.x,
                test_y_chunks=p.test_chunks.y[p.app_name],
                epochs=p.config.epochs,
                batch_size=p.config.batch_size,
                validation_split=p.config.validation_split,
                save_checkpoint=p.save_checkpoint,
            ),
        )
    else:
        res = enilm.models.utils.train.load(p.model_path_base)

    # report
    with Section("Train duration") as sec:
        sec.disp(pd.Timedelta(seconds=res.train_duration))

    with Section("Train hist") as sec:
        if p.config.epochs > 1 and p.generate_plots:
            sec.disp(
                px.line(
                    res.train_hist,
                    x=res.train_hist.index,
                    y=["val_denorm_mae", "denorm_mae"],
                )
            )
        else:
            sec.disp(res.train_hist)

    with Section("Test hist") as sec:
        sec.disp(res.test_hist)

    # sample
    if p.generate_plots:
        with Section("Sample") as sec:
            sec.disp(
                enilm.plot.with_plotly.plot_sample(
                    win_size=p.config.win_size,
                    x=p.test.x,
                    x_chunks=p.test_chunks.x,
                    y=p.test.y[p.app_name],
                    model=res.model,
                    denorm=p.denorm,
                    app_name=p.app_name,
                    plot_slice=p.plot_slice,
                )
            )

    # log
    # wandb.log({
    #     "appliane": an,
    #     "baseline": {
    #         "train_hist": wandb.Table(data=res_baseline.train_hist, columns=res_baseline.train_hist.columns),
    #         "test_hist": wandb.Table(data=res_baseline.test_hist, columns=res_baseline.test_hist.columns),
    #         "train_duration": res_baseline.train_duration,
    #     }
    # })

    return res


# wandb.finish()
