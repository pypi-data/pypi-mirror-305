from pathlib import Path
from typing import Dict

import pandas as pd

import enilm
from .train import TrainTestResult

# type aliases
ModelID = str


# TODO: global variables
metrics_names = None
cp_metrics_names = None


def _test_single_model_save(
    result, chunks, app_name, batch_size, test_res_path, with_cp
):
    rows = []
    multi_idx_tuples = []

    # for each model
    for model_id in result:
        model = result[model_id].model

        # check that all models have the same metrics
        assert metrics_names == model.metrics_names

        # check checkpoint model
        if with_cp:
            cp_model = result[model_id].checkpoint_model
            # check metrics
            assert metrics_names == cp_model.metrics_names

        # for each testset
        for testset_id in chunks:
            testset = chunks[testset_id]

            # test model
            test_res = model.evaluate(
                x=testset.x,
                y=testset.y[app_name],
                batch_size=batch_size,
            )

            # test checkpoint model
            if with_cp:
                test_res_cp = cp_model.evaluate(
                    x=testset.x,
                    y=testset.y[app_name],
                    batch_size=batch_size,
                )

            # add row of results for current mode and testset
            multi_idx_tuples.append((model_id, testset_id))
            curr_res = list(test_res)
            if with_cp:
                curr_res.extend(test_res_cp)
            rows.append(curr_res)

    # create multi-indexed dataframe for results of current repeat
    # index level 1: model
    # index level 2: testset
    columns = list(metrics_names)
    if with_cp:
        columns.extend(cp_metrics_names)
    test_res_df = pd.DataFrame(
        rows,
        columns=columns,
        index=pd.MultiIndex.from_tuples(
            multi_idx_tuples,
            names=["model_id", "set_id"],
        ),
    )
    test_res_df.to_csv(test_res_path)


def test_multi_save(
    chunks: Dict[str, enilm.etypes.xy.XYArray],
    result: Dict[ModelID, TrainTestResult],
    app_name: enilm.etypes.AppName,
    save_dir: Path,
    test_repeats: int,
    batch_size: int,
    with_cp: bool,
):
    global metrics_names, cp_metrics_names
    metrics_names = result[list(result.keys())[0]].model.metrics_names
    cp_metrics_names = [metric_name + "_cp" for metric_name in metrics_names]

    save_dir.mkdir(exist_ok=True)
    test_res_dfs = []

    # test/load results for each: repeat/model/testset
    # and save each resulting dataframe in its own file: test_res_{i}.csv (i for repeat)
    for i in range(test_repeats):
        test_res_path = Path(save_dir / f"test_res_{i}.csv")
        if not test_res_path.exists():
            _test_single_model_save(result, chunks, app_name, batch_size, test_res_path, with_cp)
        test_res_dfs.append(pd.read_csv(test_res_path))

    # all together in single multi-index df
    # index level 1: repeat
    # index level 2: model
    # index level 3: testset
    all_res_path = save_dir / "test_res_all.csv"

    # save
    if not all_res_path.exists():
        rows = []
        for repeat in range(test_repeats):
            df = test_res_dfs[repeat]
            for exp in range(len(df)):
                # exp = model + testset
                rows.append([repeat] + df.iloc[exp].to_list())

        df = pd.DataFrame(rows)

        # columns names
        columns = [
            "repeat",
            "model_id",
            "set_id",
        ] + metrics_names
        if with_cp:
            columns.extend(cp_metrics_names)
        df.columns = columns

        df.to_csv(all_res_path, index=False)

    # load
    df = pd.read_csv(all_res_path)
    df = df.set_index(["repeat", "model_id", "set_id"])

    # mean across all repeats
    df.groupby(["model_id", "set_id"]).mean().to_csv(save_dir / "test_res_all_mean.csv")

    # std across all repeats
    df.groupby(["model_id", "set_id"]).std().to_csv(save_dir / "test_res_all_std.csv")
