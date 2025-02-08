import unittest

from parameterized import parameterized

from heaps.heaps import Heap
from stacks.stack_stuff import StackStuff


class HeapStuffTests(unittest.TestCase):

    @parameterized.expand([
        (["a", "a", "b", "b", "b", "c"], 2, ["b", "a"]),
        (["a", "a", "b", "b", "b", "c"], 5, ["b", "a", "c"]),
        (["a"], 5, ["a"]),
    ])
    def test_reverse_list(self, input, k, expected):
        ss = Heap()
        assert ss.k_most_frequent_str(k, input) == expected
