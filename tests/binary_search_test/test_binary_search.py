import unittest

from parameterized import parameterized
import pytest

from binary_search.binary_search import BinarySearch


class BinarySearchTest(unittest.TestCase):

    @parameterized.expand([
        ([1, 2, 3, 4], 1, 0),
        ([1, 2, 3, 4], 2, 1),
        ([1, 2, 3, 4], 3, 2),
        ([1, 2, 3, 4], 4, 3),
        ([1], 1, 0),
        ([], 1, -1),
        ([1, 2, 3, 4], 45, -1)])
    def test_binary_search(self, input_list, target, expected):
        bs = BinarySearch()
        self.assertEqual(bs.binary_search(input_list, target), expected)
        self.assertEqual(bs.binary_search_recur(input_list, target), expected)


    @parameterized.expand([
        ([1, 2, 4, 5, 7, 8, 9], 4, 2),
        ([1, 2, 4, 5 ,7, 8, 9], 6, 4)
    ])
    def test_binary_search(self, input_list, target, expected):
        bs = BinarySearch()
        self.assertEqual(bs.find_insertion_index(input_list, target), expected)
        self.assertEqual(bs.find_insertion_index(input_list, target), expected)

    @parameterized.expand([
        ([2,6,3,8], 7, 3),
    ])
    def test_cutting_wood(self, input_list, target, expected):
        bs = BinarySearch()
        self.assertEqual(bs.cutting_wood(input_list, target), expected)
