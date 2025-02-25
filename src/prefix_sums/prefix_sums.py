from collections import Counter, defaultdict
from enum import Enum
from typing import List, Tuple


class OPERATOR(Enum):
    sum = "sum"
    product = "product"


class PREFIX_SUMS:

    def __operator_to_prefix_operator__(self, input_vals: List[int], operator: OPERATOR) -> List[int]:
        if len(input_vals) <= 1:
            return input_vals
        output = [input_vals[0]]
        for i in range(1, len(input_vals)):
            output.append(output[-1] + input_vals[i] if operator == OPERATOR.sum else output[-1] * input_vals[i])
        return output

    def __prefix_operator_to_operator__(self, input_vals: List[int], operator: OPERATOR) -> List[int]:
        if len(input_vals) <= 1:
            return input_vals
        output = [input_vals[0]]
        for i in range(1, len(input_vals)):
            output.append(
                input_vals[i] - input_vals[i - 1] if operator == OPERATOR.sum else input_vals[i] / input_vals[i - 1])
        return output

    def sum_between_ranges(self, range: Tuple[int, int], input_values: List[int]):

        if not range or not input_values:
            return 0
        sum_prefix = self.__operator_to_prefix_operator__(input_values, OPERATOR.sum)
        if range[0] == 0:
            return sum_prefix[range[1]]
        else:
            return sum_prefix[range[1]] - sum_prefix[range[0] - 1]

    def k_sum_sub_arrays(self, nums: List[int], k: int) -> int:
        # find the numer of sub-arrays in an integer array that sum to K
        sum_prefix_freq = defaultdict(int)
        sum_prefix_freq[0] += 1
        total = 0
        matches = 0
        for i in nums:
            total += i
            diff = total - k
            matches += sum_prefix_freq.get(diff, 0)
            sum_prefix_freq[total] += 1
        return matches

    def product_array_without_current_element(self, nums: List[int]):
        if len(nums) <= 1:
            return nums
        output = [1]
        for i in range(1, len(nums)):
            output.append(output[-1] * nums[i - 1])
        right_product = 1
        for i in range(len(output) - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        return output
