from linked_lists.model import SingleLinkedListNode


class DetectLinkedListLoop:

    def has_loop(self, head: SingleLinkedListNode):
        if not head or not head.next:
            return False
        slow_pointer = head
        fast_pointer = head.next

        toggle = False
        while fast_pointer and fast_pointer != slow_pointer:
            if toggle:
                slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
            toggle = (not toggle)
        return not (fast_pointer == None)