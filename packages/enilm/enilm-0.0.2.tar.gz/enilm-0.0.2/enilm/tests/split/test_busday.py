from unittest import TestCase

from enilm.etypes import Datasets
from enilm import datasets
from enilm.split.busday import *


class TestBusday(TestCase):
    def setUp(self) -> None:
        self.ds = Datasets.HIPE
        self.house = 1
        self.data = (
            datasets.loaders.load(self.ds, self.house)
            .elec.mains()
            .power_series_all_data()
        )
        return super().setUp()

    def test_split_pd_on_offday_correct_length(self):
        ondays, offdays = split_pd_on_offday(self.data, self.ds)
        self.assertEqual(self.data.shape[0], ondays.shape[0] + offdays.shape[0])
