import unittest

from hash_maps_and_sets.PairSumUnsorted import PairSumUnsorted


class HashMapAndSetsTests(unittest.TestCase):

    def test_does_return_something(self):
        pair_sum = PairSumUnsorted()
        response = pair_sum.identify_pair([-1,  3, 4, 2], 3)
        assert 0 in response
        assert 2 in response
