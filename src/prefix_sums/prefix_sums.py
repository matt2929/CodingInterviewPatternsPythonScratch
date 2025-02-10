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
