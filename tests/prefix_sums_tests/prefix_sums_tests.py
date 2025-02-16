import unittest
from parameterized import parameterized
from prefix_sums.prefix_sums import PREFIX_SUMS, OPERATOR


class PREFIX_SUMSTests(unittest.TestCase):

    @parameterized.expand([
        ([1, 2, 3], [1, 3, 6]),
    ])
    def test_prefix_sums(self, input, expected):
        prefix_sums = PREFIX_SUMS()
        assert prefix_sums.__operator_to_prefix_operator__(input, OPERATOR.sum) == expected
        assert prefix_sums.__prefix_operator_to_operator__(expected, OPERATOR.sum) == input

    @parameterized.expand([
        ([1, 2, 3], [1, 2, 6]),
    ])
    def test_prefix_product(self, input, expected):
        prefix_sums = PREFIX_SUMS()
        assert prefix_sums.__operator_to_prefix_operator__(input, OPERATOR.product) == expected
        assert prefix_sums.__prefix_operator_to_operator__(expected, OPERATOR.product) == input

    @parameterized.expand([
        ([0, 3], [3, -7, 6, 0, -2, 5], 2),
        ([2, 4], [3, -7, 6, 0, -2, 5], 4),
        ([2, 2], [3, -7, 6, 0, -2, 5], 6),
        ([0, 5], [3, -7, 6, 0, -2, 5], 5),  # Sum of entire list
        ([1, 3], [3, -7, 6, 0, -2, 5], -1),  # Middle range including negative number
        ([3, 5], [3, -7, 6, 0, -2, 5], 3),  # Range ending at last index
        ([4, 4], [3, -7, 6, 0, -2, 5], -2),  # Single negative number
        ([0, 0], [3, -7, 6, 0, -2, 5], 3),  # Single positive number
        ([0, 2], [-1, -2, -3, 4, 5, 6], -6),  # All negative numbers in range
        ([2, 5], [1, 2, 3, 4, 5, 6], 18),  # Consecutive numbers
        ([1, 1], [0, 10, 20, 30, 40], 10),  # Single value in positive list

        ([0, 0], [], 0),  # Edge case: empty list (should return 0 or handle gracefully)

    ])
    def test_sum_between_ranges(self, range, sum_list, expected):
        prefix_sums = PREFIX_SUMS()
        assert prefix_sums.sum_between_ranges(range, sum_list) == expected

    @parameterized.expand([
        ([1, 2, -1, 1, 2], 3, 3),
        ([], 3, 0),
        ([1, 2, 3], 7, 0),
        ([5], 5, 1),
        ([5], 3, 0),
        ([1, -1, 1, -1], 0, 4),
        ([-1, -2, -3, -4], -3, 2),
        ([1, 2, 3, 4], 5, 1),  # Fixed expected output from 2 to 1
        ([1, 2, -1, 2, 1, 2], 3, 4),
        ([1, 1, 1, 1, 1], 2, 4),
        ([1, 2, 3], 6, 1),
        ([1000, 1000, 1000, 1000], 2000, 3),
        ([1, 2, 3, 4], 1000, 0),
    ])
    def test_k_sum_sub_arrays(self, sum_list, k, expected):
        prefix_sums = PREFIX_SUMS()

        assert prefix_sums.k_sum_sub_arrays(k=k, nums=sum_list) == expected

    @parameterized.expand([
        ([2, 3, 1, 4, 5], [60, 40, 120, 30, 24]),
    ])
    def test_product_array_without_current_element(self, sum_list, expected):
        prefix_sums = PREFIX_SUMS()

        assert prefix_sums.product_array_without_current_element(nums=sum_list) == expected
