import unittest

from hash_maps_and_sets.SudokuVerification import SudokuVerification


class SudokuVerificationTest(unittest.TestCase):

    def test_does_return_something(self):
        sudoku_verifier = SudokuVerification()
        response = sudoku_verifier.verify(
            [
                [3, None, 6, None, 5, 8, 4, None, None],
                [5, 2, None, None, None, None, None, None, None],
                [None, 8, 7, None, None, None, None, 3, 1],
                [1, None, None, 5, None, None, 3, 2, None],
                [9, None, None, 8, 6, 3, None, None, 5],
                [None, 5, None, None, 9, None, 6, None, None],
                [None, 3, None, None, None, None, 2, 5, None],
                [None, 1, None, None, None, None, None, 7, 4],
                [None, None, 5, 2, None, 6, None, None, None],
            ]
        )
        assert response == True
