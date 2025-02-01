from linked_lists.model import SingleLinkedListNode


class SingleLinkedListReversal:

    def reverse_single_linked_list(self, ll: SingleLinkedListNode):

        if not ll.next:
            return ll
        pntr_1=None
        pntr_2=ll
        while(pntr_2):
            pntr_3 = pntr_2.next
            pntr_2.next = pntr_1
            pntr_1=pntr_2
            pntr_2=pntr_3
        return pntr_1

    def reverse_single_linked_list_recur(self, ll: SingleLinkedListNode):
        if not ll or not ll.next:
            return ll

        new_head = self.reverse_single_linked_list(ll.next)
        ll.next.next = ll
        ll.next=None
        return new_head