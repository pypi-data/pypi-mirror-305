from unittest import TestCase

from enilm.dicthelpers.nested import *


class TestNested(TestCase):
    def test_check_in_nested_dict(self):
        _dict = {"a": {"b": {"c": {"d": "abcd"}}}}

        self.assertTrue(check_in_nested_dict(_dict, "abcd"))
        self.assertTrue(check_in_nested_dict(_dict, "abcdd"))
        self.assertTrue(check_in_nested_dict(_dict, "abc"))
        self.assertTrue(check_in_nested_dict(_dict, "a"))

        self.assertFalse(check_in_nested_dict(_dict, "abca"))
        self.assertFalse(check_in_nested_dict(_dict, "aa"))

    def test_put_in_nested_dict(self):
        _dict = {}
        put_in_nested_dict(_dict, "abcd", "value at abcd")
        self.assertEqual(_dict, {"a": {"b": {"c": {"d": "value at abcd"}}}})
