import unittest

from linked_lists.find_linked_list_midpoint import LinkedListMidPoint
from linked_lists.model import SingleLinkedListNode


class LinkedListMidPointTest(unittest.TestCase):
    """
    Given a singly linked list, find and return its middle node. If there are two middle nodes, return the second one.
    """

    def test_find_midpoint_val(self):
        midpoint_detector = LinkedListMidPoint()
        root = SingleLinkedListNode(0)
        assert midpoint_detector.find_midpoint_val(root) == 0
        root.next = SingleLinkedListNode(1)
        assert midpoint_detector.find_midpoint_val(root) == 1
        root.next.next = SingleLinkedListNode(2)
        assert midpoint_detector.find_midpoint_val(root) == 1
        root.next.next.next = SingleLinkedListNode(3)
        assert midpoint_detector.find_midpoint_val(root) == 2
        root.next.next.next.next = SingleLinkedListNode(4)
        assert midpoint_detector.find_midpoint_val(root) == 2
