from math import floor
from typing import List


class BinarySearch:

    def binary_search(self, input: List[int], search: int):
        if len(input) == 0:
            return -1
        pntr_left = 0
        pntr_right = len(input) - 1
        while pntr_left <= pntr_right:
            middle_index = pntr_left + ((pntr_right - pntr_left) // 2)

            if input[middle_index] == search:
                return middle_index
            elif input[middle_index] < search:
                pntr_left = middle_index + 1
            else:
                pntr_right = middle_index - 1
        return -1

    def binary_search_recur(self, input: List[int], search: int):
        return self.__binary_search_recur_helper__(input, search, 0, len(input) - 1)

    def __binary_search_recur_helper__(self, input: List[int], search: int, left: int, right: int):
        if left > right:
            return -1
        if input[self.__middle_index__(left, right)] == search:
            return self.__middle_index__(left, right)
        elif input[self.__middle_index__(left, right)] < search:
            return self.__binary_search_recur_helper__(input, search, self.__middle_index__(left, right) + 1, right)
        else:
            return self.__binary_search_recur_helper__(input, search, left, self.__middle_index__(left, right) - 1)

    def __middle_index__(self, left: int, right: int):
        return left + ((right - left) // 2)

    def find_insertion_index(self, input_arr: List[int], target: int):
        """
        You are given a sorted array that contains unique values, along with a n integer target.
        * if the array contains the target value return the index.
        * otherwise return the insertion index. This is the index where the target would be if it were interacted in order,
         maintaining the sorted sequence of the array.
        """
        return self.__find_insertion_index__(input_arr, target, 0, len(input_arr) - 1)

    def __find_insertion_index__(self, input: List[int], search: int, left: int, right: int):
        if left > right:
            return left
        if input[self.__middle_index__(left, right)] == search:
            return self.__middle_index__(left, right)
        elif input[self.__middle_index__(left, right)] < search:
            return self.__find_insertion_index__(input, search, self.__middle_index__(left, right) + 1, right)
        else:
            return self.__find_insertion_index__(input, search, left, self.__middle_index__(left, right) - 1)

    def cutting_wood(self, input_wood: List[int], at_least: int) -> int:
        return self.__cutting_wood_recur_helper__(input_wood, at_least, 0, max(input_wood))

    def determine_wood_at_height(self, input_wood: List[int], height: int):
        return sum((wood - height) if wood > height else 0 for wood in input_wood)

    def __cutting_wood_recur_helper__(self, input: List[int], search: int, left: int, right: int):
        if left > right:
            return left
        found = self.determine_wood_at_height(input, self.__middle_index__(left, right) + 1)
        print(f"\n{left} {right} {found} looking for {search}")
        if found == search:
            return self.__middle_index__(left, right)
        elif found < search:
            return self.__cutting_wood_recur_helper__(input, search, left, self.__middle_index__(left, right) - 1)
        else:
            return self.__cutting_wood_recur_helper__(input, search, self.__middle_index__(left, right) + 1, right)
