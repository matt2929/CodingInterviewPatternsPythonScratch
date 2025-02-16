import dataclasses
from collections import deque
from typing import List, Optional


class TREES:
    ...


@dataclasses.dataclass
class TreeNode:
    val: int
    left: 'TreeNode' = None
    right: 'TreeNode' = None

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
