from linked_lists.model import SingleLinkedListNode


class SingleLinkedListReversal:

    def reverse_single_linked_list(self, ll: SingleLinkedListNode):

        if not ll.next:
            return ll

        pntr_1=ll
        pntr_2=ll.next
        pntr_3=ll.next.next
        pntr_1.next = None
        while(pntr_3):
            pntr_2.next = pntr_1
            pntr_1=pntr_2
            pntr_2=pntr_3
            pntr_3=pntr_3.next
        pntr_2.next = pntr_1
        return pntr_2
