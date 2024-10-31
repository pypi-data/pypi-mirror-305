from unittest import TestCase

import enilm

class TestLoaders(TestCase):
    def test_load_multiple_seps(self):
        ds = enilm.etypes.Datasets.HIPE_WEEK
        res = enilm.datasets.loaders.load_multiple_seps(
            datasets=[ds],
            physical_quantity_and_ac_type={ds: {'mains': ('power', 'apparent'), 'app': ('power', 'active')}},
            houses_per_ds={ds: [1]},
            apps_per_ds={ds: enilm.datasets.loaders.load(ds, 1).elec.appliances},
        )
        self.assertEqual(res.data[ds][1]["mains"]["full"].shape[0], 110492)
        