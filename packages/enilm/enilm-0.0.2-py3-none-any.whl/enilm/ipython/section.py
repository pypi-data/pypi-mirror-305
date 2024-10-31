from typing import Any

from IPython.display import HTML, display
import pandas as pd
from plotly.graph_objects import Figure


class Section(object):
    def __init__(self, title: str, expand: bool = True):
        self.title = title
        self.expand = expand
        self.html = ""

    def disp(self, what: Any):
        if isinstance(what, pd.DataFrame):
            self.html += what.to_html()
        if isinstance(what, Figure):
            from plotly.io import to_html

            self.html += to_html(what, full_html=False)
        else:
            self.html += str(what)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        display(
            HTML(
                f"""
            <details {"open" if self.expand else ""}>
                <summary><b>{self.title}</b></summary>
                {self.html}
            </details>
            """
            )
        )
