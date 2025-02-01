import math
from typing import List


class HappyNumberCalculator:

    def is_happy_number(self, happy_number: int) -> bool:
        pntr_1 = happy_number
        pntr_2 = self.compute_next(happy_number)
        skip_track = False
        while pntr_2 != 1 and pntr_1 != pntr_2:
            pntr_2 = self.compute_next(input_num=pntr_2)
            if skip_track:
                pntr_1 = self.compute_next(input_num=pntr_1)
            skip_track = not skip_track
        return pntr_2 == 1

    def compute_next(self, input_num: int) -> int:
        total = 0
        numbers = self.split_int_to_list(input_num)
        for num in numbers:
            total += math.pow(num, 2)
        return total

    def split_int_to_list(self, int_to_split: int) -> List[int]:
        output = []
        while int_to_split > 0:
            output.append(int_to_split % 10)
            int_to_split = int_to_split // 10
        output.reverse()
        return output
