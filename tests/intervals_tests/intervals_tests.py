import unittest
from parameterized import parameterized
from intervals.intervals import INTERVALS


class INTERVALSTests(unittest.TestCase):

    @parameterized.expand([
        ([(0, 1), (0, 1)], True),
        ([(0, 2), (1, 3)], True),
        ([(0, 2), (2, 3)], True),
        ([(1, 3), (0, 2)], True),
        ([(2, 3), (0, 2)], True),
        ([(0, 1), (2, 3)], False),
        ([(0, 1), (2, 3)], False),
    ])
    def test_intervals(self, input, expected):
        intervals = INTERVALS()
        assert intervals.do_intervals_overlap(input[0], input[1]) == expected

    @parameterized.expand([
        (
                [
                    (0, 1), (0, 1)
                ],
                [
                    (0, 1)
                ]
        ),
        (
                [
                    (3, 4), (7, 8), (2, 5), (6, 7), (1, 4)
                ],
                [
                    (1, 5), (6, 8)
                ]
        ),
    ])
    def test_overlapping_intervals(self, input, expected):
        intervals = INTERVALS()
        assert intervals.merge_overlapping_intervals(input) == expected

    @parameterized.expand([
        (
                [
                    (1, 4), (5, 6), (9, 10)
                ],
                [
                    (2, 7), (8, 9)
                ],
                [
                    (2, 4), (5, 6), (9, 9)
                ]
        ),
        (
                [
                    (1, 2), (3, 4), (5, 6)
                ],
                [
                    (1,5)
                ],
                [
                    (1, 2), (3, 4), (5, 5)
                ]
        )
    ])
    def test_overlapping_intervals(self, input_1, input_2, expected):
        intervals = INTERVALS()
        assert intervals.identify_all_interval_overlaps(input_1, input_2) == expected
