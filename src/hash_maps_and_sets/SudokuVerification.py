from collections import defaultdict
from typing import List, Dict

"""
Given a partially complete 9x9 sudoku board, determine if the current state of the board adheres to the rules of the game: 
* each row and column must contain unique numbers between 1 and 9 or be empty 
* each of the nine 3x3 sub-grids the compose the grid must contain unique numbers between 1 and 9 or be empty 

Note: you are asked to determine whether the current state of the board is valid given the rules, not if the board is solvable. 
"""


class SudokuVerification:

    def verify(self, input: List[List[int]], defaultset=None) -> bool:
        latitude_sets = defaultdict(set)
        longitude_sets = defaultdict(set)
        graph_sets = {}
        for i in range(3):
            graph_sets[i]={}
            for j in range(3):
                graph_sets[i][j] = set()
        for index_x, list_x in enumerate(input):
            for index_y, value_at_coordinate in enumerate(list_x):
                if not value_at_coordinate:
                    continue
                if (value_at_coordinate in longitude_sets[index_x]
                        or value_at_coordinate in latitude_sets[index_y]
                        or value_at_coordinate in graph_sets[index_x // 3][index_y // 3]
                ):
                    return False
                longitude_sets[index_x].add(value_at_coordinate)
                latitude_sets[index_y].add(value_at_coordinate)
                graph_sets[index_x // 3][index_y // 3].add(value_at_coordinate)
        return True
