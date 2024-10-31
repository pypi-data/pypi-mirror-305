"""Generate notebook reports"""

from pathlib import Path
from typing import Optional

import papermill as pm

curr_file_dir = Path(__file__).parent


def nb_to_html(nb: Path, output_html: Optional[Path] = None):
    if output_html.suffix == 'html':
        raise ValueError('Output html must end with html')

    # https://stackoverflow.com/a/65502489
    import nbformat
    from nbconvert.preprocessors import ExecutePreprocessor
    from nbconvert import HTMLExporter

    # read source notebook
    with open(nb) as f:
        nb = nbformat.read(f, as_version=4)

    # export to html
    html_exporter = HTMLExporter()
    html_exporter.exclude_input = False
    html_data, resources = html_exporter.from_notebook_node(nb)

    # write to output file
    with open(output_html, "w") as f:
        f.write(html_data)


def gen_nb(exp_res_dir: Path, output_nb: Path, output_html: Optional[Path] = None):
    if output_nb.suffix == 'ipynb':
        raise ValueError('Output notebook must end with ipynb')

    pm.execute_notebook(
        curr_file_dir / 'template.ipynb',
        output_nb,
        parameters=dict(
            base_dir=str(exp_res_dir),
        )
    )

    # convert to html
    if output_html is not None:
        nb_to_html(output_nb, output_html)
