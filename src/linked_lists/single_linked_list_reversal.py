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
