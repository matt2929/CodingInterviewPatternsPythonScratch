import dataclasses
from collections import deque
from typing import List, Optional


class TREES:
    ...

best_path_dict = {}
@dataclasses.dataclass
class TreeNode:
    val: int
    left: 'TreeNode' = None
    right: 'TreeNode' = None
    lca = None

    def pre_order_traversal(self):
        output = []
        self.__helper_pre_order_traversal__(self, output)
        return output

    def __helper_pre_order_traversal__(self, node: 'TreeNode', output: List['TreeNode']):
        if not node:
            return
        output.append(node.val)
        self.__helper_pre_order_traversal__(node.left, output)
        self.__helper_pre_order_traversal__(node.right, output)

    def in_order_traversal(self):
        output = []
        self.__helper_in_order_traversal__(self, output)
        return output

    def __helper_in_order_traversal__(self, node: 'TreeNode', output: List['TreeNode']):
        if not node:
            return
        self.__helper_in_order_traversal__(node.left, output)
        output.append(node.val)
        self.__helper_in_order_traversal__(node.right, output)

    def post_order_traversal(self):
        output = []
        self.__helper_post_order_traversal__(self, output)
        return output

    def __helper_post_order_traversal__(self, node: 'TreeNode', output: List['TreeNode']):
        if not node:
            return
        self.__helper_post_order_traversal__(node.left, output)
        self.__helper_post_order_traversal__(node.right, output)
        output.append(node.val)

    def bfs(self, search: int) -> Optional['TreeNode']:
        queue = [self]
        while queue:
            print(queue[0].val)
            node = queue.pop()
            if node.val == search:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs(self, search: int) -> Optional['TreeNode']:
        stack = deque([self])
        while stack:
            print(stack[0].val)
            node = stack.pop()
            if node.val == search:
                return node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    def invert_binary_tree_recur(self) -> Optional['TreeNode']:
        self.__invert_binary_tree_helper__(self)
        return self

    def invert_binary_tree_iterative(self) -> Optional['TreeNode']:
        queue = deque([self])
        while queue:
            node = queue.pop()
            if node.left and node.right:
                temp = node.right
                node.right = node.left
                node.left = temp
                queue.append(node.left)
                queue.append(node.right)
            elif node.left:
                node.right = node.left
                node.left = None
                queue.append(node.right)
            elif node.right:
                node.left = node.right
                node.right = None
                queue.append(node.left)
        return self

    def __invert_binary_tree_helper__(self, node: Optional['TreeNode']):
        if not node:
            return None
        if node.left and node.right:
            temp = node.right
            node.right = node.left
            node.left = temp
        elif node.left:
            node.right = node.left
            node.left = None
        elif node.right:
            node.left = node.right
            node.right = None
        self.__invert_binary_tree_helper__(node.left)
        self.__invert_binary_tree_helper__(node.right)

    def is_tree_balanced_iterative(self):
        if not self:
            return True

        stack = deque()
        node_heights = {}  # Store heights using node ID
        stack.append(self)

        while stack:
            node = stack[-1]

            # Postorder traversal: visit left and right before processing node
            if node.left and id(node.left) not in node_heights:
                stack.append(node.left)
            elif node.right and id(node.right) not in node_heights:
                stack.append(node.right)
            else:
                stack.pop()  # Process the node
                print(f"\nnode: {node.val}")
                left_height = node_heights.get(id(node.left), 0)
                right_height = node_heights.get(id(node.right), 0)

                # If height difference is greater than 1, tree is unbalanced
                if abs(left_height - right_height) > 1:
                    return False

                # Store the height using node's unique ID
                node_heights[id(node)] = 1 + max(left_height, right_height)

        return True

    def is_tree_balanced_recursive(self):
        return self.is_tree_balanced_recursive_helper(self) != -1

    def is_tree_balanced_recursive_helper(self, node: 'TreeNode') -> int:
        if not node:
            return 0
        left = self.is_tree_balanced_recursive_helper(node.left)
        right = self.is_tree_balanced_recursive_helper(node.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    def find_right_most_level(self) -> List['TreeNode']:
        queue = deque([(self)])
        output = []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == size - 1:
                    output.append(node)
        return output

    def determine_widest_binary_tree_level(self) -> int:
        queue = deque([(self, 0)])
        max_spread = 0
        while queue:
            depth = len(queue)
            sub_min = None
            for i in range(depth):
                node, index_depth = queue.popleft()
                if node:
                    if sub_min is None:
                        sub_min = index_depth
                    sub_max = index_depth
                    max_spread = max((sub_max - sub_min) + 1, max_spread)
                    queue.append((node.left, index_depth * 2))
                    queue.append((node.right, (index_depth * 2) + 1))
        return max_spread

    def is_valid_binary_search_tree(self) -> bool:
        queue = deque([(self, None, None)])
        while queue:
            node, lower, upper = queue.popleft()
            if (lower and lower >= node.val) or (upper and node.val >= upper):
                return False
            if node.left:
                queue.append((node.left, lower, node.val))
            if node.right:
                queue.append((node.right, node.val, upper))
        return True

    def lowest_common_ancestor(self, target1: int, target2: int) -> 'TreeNode':
        return self.__lowest_common_ancestor__(self, target1, target2)

    def __lowest_common_ancestor__(self, node: 'TreeNode', target1: int, target2: int) -> 'TreeNode':
        if not node:
            return None
        if node.val == target1 or node.val == target2:
            return node
        left_hunt = self.__lowest_common_ancestor__(node.left, target1, target2)
        right_hunt = self.__lowest_common_ancestor__(node.right, target1, target2)
        if left_hunt and right_hunt:
            return node
        return left_hunt if left_hunt else right_hunt

    def maximum_sum_of_a_continuous_path(self):
        queue = deque([self])
        max_path = None
        while queue:
            node = queue.popleft()
            best_path = self.best_path_from_root(node)
            if not max_path:
                max_path = best_path
            max_path = max(best_path, max_path)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return max_path

    def best_path_from_root(self, node: 'TreeNode'):
        left = self.best_path_sum(node.left)
        right = self.best_path_sum(node.right)
        sum = node.val
        if left > 0:
            sum += left
        if right > 0:
            sum += right
        return sum



    def best_path_sum(self, node: 'TreeNode'):
        global best_path_dict

        if not node:
            return 0
        if node.left:
            left = best_path_dict.get(node.left.val, self.best_path_sum(node.left))
            best_path_dict[node.left.val] = left
        else:
            left = 0
        if node.right:
            right = best_path_dict.get(node.right.val, self.best_path_sum(node.right))
            best_path_dict[node.right.val] = right
        else:
            right = 0
        if left < 0 and right < 0:
            return node.val
        new_sum = max(left, right) + node.val
        print(f"{node.val} - {new_sum}")
        return new_sum
