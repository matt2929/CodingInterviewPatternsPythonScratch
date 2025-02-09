import copy
import unittest

from parameterized import parameterized

from heaps.heaps import Heap
from linked_lists.model import SingleLinkedListNode
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

    def test_combined_linked_list(self):
        input_test = [
            SingleLinkedListNode(1, SingleLinkedListNode(6, None)),
            SingleLinkedListNode(1, SingleLinkedListNode(4, SingleLinkedListNode(6, None))),
            SingleLinkedListNode(3, SingleLinkedListNode(7, None)),
        ]
        ss = Heap()
        output_head = ss.combine_linked_lists(input_test)
        assert output_head.linked_list_as_array_str() == "[1, 1, 3, 4, 6, 6, 7]"

    count_to_8 = [0, 1, 2, 2, 3, 4, 5, 7, 8]
    count_to_8_reverse = [i for i in count_to_8]
    count_to_8_reverse.reverse()
    @parameterized.expand([
        (count_to_8, 3),
        (count_to_8_reverse, 3),
        ([0, 1, 2], 1),
        ([4, 3, 1, 10], 3.5),
    ])
    def test_reverse_list(self, input_list, expected):
        ss = Heap()
        assert ss.find_median(input_list) == expected
