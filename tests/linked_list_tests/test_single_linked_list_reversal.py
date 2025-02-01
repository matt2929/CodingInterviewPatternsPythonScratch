import unittest

from linked_lists.model import SingleLinkedListNode
from linked_lists.single_linked_list_reversal import SingleLinkedListReversal


class SingleLinkListReversalTest(unittest.TestCase):

    def test_reversal(self):
        single_link_list_reversal = SingleLinkedListReversal()

        # 1
        n1 = SingleLinkedListNode(1, None)
        response = single_link_list_reversal.reverse_single_linked_list_recur(n1)
        assert "[1]" == response.linked_list_as_array_str()

        # 2
        n1 = SingleLinkedListNode(1, None)
        n1.next = SingleLinkedListNode(2, None)
        response = single_link_list_reversal.reverse_single_linked_list_recur(n1)
        assert "[2, 1]" == response.linked_list_as_array_str(), response.linked_list_as_array_str()

        # 3
        n1 = SingleLinkedListNode(1, None)
        n1.next = SingleLinkedListNode(2, None)
        n1.next.next = SingleLinkedListNode(3, None)
        response = single_link_list_reversal.reverse_single_linked_list_recur(n1)
        assert "[3, 2, 1]" == response.linked_list_as_array_str()

        # 4
        n1 = SingleLinkedListNode(1, None)
        n1.next = SingleLinkedListNode(2, None)
        n1.next.next = SingleLinkedListNode(3, None)
        n1.next.next.next = SingleLinkedListNode(4, None)
        response = single_link_list_reversal.reverse_single_linked_list_recur(n1)
        assert "[4, 3, 2, 1]" == response.linked_list_as_array_str()
