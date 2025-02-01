import math
import unittest
from typing import List

from linked_lists.happy_number_calculator import HappyNumberCalculator


class HappyNumberCalculatorTest(unittest.TestCase):

    def test_is_happy_number(self):
        calc = HappyNumberCalculator()
        assert calc.is_happy_number(0) == False
        assert calc.is_happy_number(1) == True
        assert calc.is_happy_number(23) == True
        assert calc.is_happy_number(116) == False

    def test_split_int_to_list(self):
        calc = HappyNumberCalculator()
        assert calc.split_int_to_list(1) == [1]
        assert calc.split_int_to_list(12) == [1, 2]
        assert calc.split_int_to_list(123) == [1, 2, 3]
        assert calc.split_int_to_list(1234) == [1, 2, 3, 4]
        assert calc.split_int_to_list(12345) == [1, 2, 3, 4, 5]

    def test_compute_happy_number(self):
        calc = HappyNumberCalculator()
        assert calc.compute_next(1) == 1
        assert calc.compute_next(12) == 5
        assert calc.compute_next(123) == 14
        assert calc.compute_next(1234) == 30
        assert calc.compute_next(12345) == 55
        assert calc.compute_next(116) == 38
        assert calc.compute_next(38) == 73
        assert calc.compute_next(73) == 58
