from linked_lists.model import SingleLinkedListNode


class LinkedListMidPoint:
    """
    Given a singly linked list, find and return its middle node. If there are two middle nodes, return the second one.
    """
    def find_midpoint_val(self, root: SingleLinkedListNode):
        slow = root
        fast = root
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.val
