# for each zero in an m x n matrix, set its entire row and column to zero in place.
from typing import List


class ZeroStripping:

    def perform_zero_strip(self, input_matrix: List[List[int]]):
        x_marks = set()
        y_marks = set()
        for index_x, column in enumerate(input_matrix):
            for index_y, value in enumerate(column):
                if value == 0:
                    x_marks.add(index_x)
                    y_marks.add(index_y)

        for x_mark in x_marks:
            for y in range(len(input_matrix[x_mark])):
                input_matrix[x_mark][y]=0

        for y_mark in y_marks:
            for x in range(len(input_matrix)):
                input_matrix[x][y_mark]=0

        return input_matrix