import unittest

import pytest
from parameterized import parameterized
from trees.trees import TreeNode


class TREESTests(unittest.TestCase):

    def __test_tree_a__(self) -> 'TreeNode':
        trees1 = TreeNode(1)
        trees2 = TreeNode(2)
        trees3 = TreeNode(3)
        trees4 = TreeNode(4)
        trees5 = TreeNode(5)
        trees6 = TreeNode(6)
        trees7 = TreeNode(7)
        trees1.left = trees2
        trees1.right = trees3
        trees2.left = trees4
        trees2.right = trees5
        trees3.left = trees6
        trees6.left = trees7
        return trees1

    def __test_tree_b__(self) -> 'TreeNode':
        trees1 = TreeNode(1)
        trees2 = TreeNode(2)
        trees3 = TreeNode(3)
        trees4 = TreeNode(4)
        trees5 = TreeNode(5)
        trees6 = TreeNode(6)
        trees7 = TreeNode(7)
        trees9 = TreeNode(9)
        trees5.left = trees2
        trees5.right = trees7
        trees2.left = trees1
        trees2.right = trees4
        trees4.left = trees3
        trees7.right = trees9
        trees9.left = trees6
        return trees5

    def __test_tree_c__(self) -> 'TreeNode':
        trees1 = TreeNode(1)
        trees2 = TreeNode(2)
        trees3 = TreeNode(3)
        trees4 = TreeNode(4)
        trees5 = TreeNode(5)
        trees6 = TreeNode(6)
        trees8 = TreeNode(8)
        trees9 = TreeNode(9)
        trees11 = TreeNode(11)
        trees1.left = trees2
        trees1.right = trees3
        trees2.left = trees4
        trees2.right = trees5
        trees4.left = trees8
        trees4.right = trees9
        trees5.right = trees11
        trees3.left = trees6
        return trees1

    def __test_tree_d__(self) -> 'TreeNode':
        trees1 = TreeNode(1)
        trees2 = TreeNode(2)
        trees3 = TreeNode(3)
        trees4 = TreeNode(4)
        trees5 = TreeNode(5)
        trees7 = TreeNode(7)
        trees8 = TreeNode(8)
        trees9 = TreeNode(9)
        trees11 = TreeNode(11)
        trees14 = TreeNode(14)
        trees1.left = trees2
        trees1.right = trees3
        trees2.left = trees4
        trees2.right = trees5
        trees4.left = trees8
        trees4.right = trees9
        trees5.right = trees11
        trees3.right = trees7
        trees7.left = trees14
        return trees1

    def test_trees(self):
        output = self.__test_tree_a__().pre_order_traversal()
        assert output == [1, 2, 4, 5, 3, 6, 7]
        output = self.__test_tree_a__().in_order_traversal()
        assert output == [4, 2, 5, 1, 7, 6, 3]
        output = self.__test_tree_a__().post_order_traversal()
        assert output == [4, 5, 2, 7, 6, 3, 1]
        invert_output = self.__test_tree_a__().invert_binary_tree_recur().in_order_traversal()
        assert invert_output == [3, 6, 7, 1, 5, 2, 4]
        invert_output = self.__test_tree_a__().invert_binary_tree_iterative().in_order_traversal()
        assert invert_output == [3, 6, 7, 1, 5, 2, 4]
        assert self.__test_tree_b__().is_tree_balanced_iterative() == False
        assert self.__test_tree_b__().is_tree_balanced_recursive() == False
        assert [i.val for i in self.__test_tree_c__().find_right_most_level()] == [1, 3, 6, 11]
        assert self.__test_tree_d__().determine_widest_binary_tree_level() == 7
    @parameterized.expand([
        # Original test case (corrected after verification)
        (1, True),
        (2, True),
        (3, True),
        (4, True),
        (5, True),
        (6, True),
        (7, True),
        (8, False),
        (0, False),
        (None, False)
    ])
    def test_search(self, search_for, expectation):
        assert (self.__test_tree_a__().bfs(search_for) != None) == expectation
        assert (self.__test_tree_a__().dfs(search_for) != None) == expectation
