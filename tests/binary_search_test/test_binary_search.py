import unittest

from binary_search.binary_search import BinarySearch


class BinarySearchTest(unittest.TestCase):

    def test_binary_search(self):
        bs = BinarySearch()
        assert bs.binary_search([1, 2, 3, 4], 1) == 0
        assert bs.binary_search([1, 2, 3, 4], 2) == 1
        assert bs.binary_search([1, 2, 3, 4], 3) == 2
        assert bs.binary_search([1, 2, 3, 4], 4) == 3
        assert bs.binary_search([1], 1) == 0
        assert bs.binary_search([], 1) == -1
        assert bs.binary_search([1, 2, 3, 4], 45) == -1
