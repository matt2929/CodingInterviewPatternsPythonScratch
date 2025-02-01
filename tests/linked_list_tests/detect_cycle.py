import unittest

from linked_lists.detect_loop_linked_list import DetectLinkedListLoop
from linked_lists.model import SingleLinkedListNode


class DetectCycle(unittest.TestCase):

    def test_detect_cycle(self):
        dlll = DetectLinkedListLoop()
        assert dlll.has_loop(None) == False
        root = SingleLinkedListNode(val=1)
        assert dlll.has_loop(root) == False
        root.next = SingleLinkedListNode(val=2)
        assert dlll.has_loop(root) == False
        root.next.next = SingleLinkedListNode(val=3)
        assert dlll.has_loop(root) == False
        root.next.next.next = SingleLinkedListNode(val=4)
        assert dlll.has_loop(root) == False
        root.next.next.next.next = SingleLinkedListNode(val=4)
        assert dlll.has_loop(root) == False
        root.next.next.next.next.next = SingleLinkedListNode(val=4)
        assert dlll.has_loop(root) == False
        root.next.next.next = root.next.next
        assert dlll.has_loop(root) == True
