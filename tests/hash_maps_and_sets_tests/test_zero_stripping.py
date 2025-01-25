# for each zero in an m x n matrix, set its entire row and column to zero in place.
import unittest
from typing import List

from hash_maps_and_sets.ZeroStripping import ZeroStripping


class ZeroStrippingTests(unittest.TestCase):

    def test_zero_stripping(self):
        zero_stripping = ZeroStripping()
        input_1 = [
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
        ]
        assert input_1 == zero_stripping.perform_zero_strip(input_1)
        input_2 = [
            [1, 2, 3],
            [1, 0, 3],
            [1, 2, 3],
        ]
        expected_2 = [
            [1, 0, 3],
            [0, 0, 0],
            [1, 0, 3],
        ]
        assert expected_2 == zero_stripping.perform_zero_strip(input_2)