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
                    (1, 5)
                ],
                [
                    (1, 2), (3, 4), (5, 5)
                ]
        )
    ])
    def test_overlapping_intervals(self, input_1, input_2, expected):
        intervals = INTERVALS()
        assert intervals.identify_all_interval_overlaps(input_1, input_2) == expected

    @parameterized.expand([
        # Original test case (corrected after verification)
        ([(1, 5), (2, 6), (3, 7), (4, 8), (5, 9)], 4),

        # Case: Non-overlapping intervals (each starts after the previous ends)
        ([(1, 2), (3, 4), (5, 6)], 1),  # No overlap at any time

        # Case: Fully nested intervals
        ([(1, 10), (2, 9), (3, 8), (4, 7)], 4),  # All active at time 4

        # Case: Intervals touching at endpoints (should not count as overlapping)
        ([(1, 2), (2, 3), (3, 4), (4, 5)], 1),  # Each interval ends where the next starts

        # Case: Large number of overlapping intervals
        ([(1, 5), (2, 6), (3, 7), (4, 8), (5, 9)], 4),  # Confirmed max overlap at 4

        # Case: Single interval (should return 1)
        ([(1, 10)], 1),

        # Case: Empty input (should return 0)
        ([], 0),

        # Case: Multiple intervals with different overlap groups
        ([(1, 5), (2, 3), (4, 7), (6, 8), (7, 10), (9, 12)], 2),

        # Case: Intervals ending where others start
        ([(1, 3), (3, 6), (6, 9)], 1),  # No true overlap since each ends before the next starts

        # Case: All intervals starting at the same time
        ([(1, 4), (1, 5), (1, 6), (1, 7)], 4),  # All active at time 1

        # Case: Multiple overlapping but not all at once
        ([(1, 3), (2, 4), (3, 5), (4, 6)], 2),  # Overlap of at most 2 at any time
    ])
    def test_biggest_overlapping_set(self, input_1, expected):
        intervals = INTERVALS()
        assert intervals.biggest_overlap(input_1) == expected
        assert intervals.biggest_overlap_book_suggestion(input_1) == expected
