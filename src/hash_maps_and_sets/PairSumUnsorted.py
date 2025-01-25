# Given an array of integers return the indexes of any two pointers numbers that
# add up to a target. The order of the indexes in the result doesn't matter.
# If no pair is found return an empty array.
from collections import defaultdict
from typing import List, Optional, Tuple


class PairSumUnsorted:

    def identify_pair(self, input: List[int], target: int) -> Optional[Tuple[int, int]]:
        potential_pair = {}
        for index, value in enumerate(input):
            compliment = target - value
            if compliment in potential_pair:
                return index, potential_pair[compliment]
            potential_pair[value] = index
        return None
