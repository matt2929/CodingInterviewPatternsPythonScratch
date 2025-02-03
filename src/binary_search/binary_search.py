from math import floor
from typing import List


class BinarySearch:

    def binary_search(self, input: List[int], search: int):
        if len(input) == 0:
            return -1
        left_pntr = 0
        right_pntr = len(input)-1
        while left_pntr <= right_pntr:
            middle_index = (left_pntr + right_pntr) // 2
            if search == input[middle_index]:
                return middle_index
            elif search > input[middle_index]:
                left_pntr = middle_index + 1
            else:
                right_pntr = middle_index - 1
        return -1
