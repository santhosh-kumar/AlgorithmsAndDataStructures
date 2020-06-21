"""
Bottom View of Binary Tree

Bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom.
Given a binary tree, print the top view of it. The output nodes can be printed in any order.

For example:

       1
    /     \
   2       3
  /  \    / \
 4    5  6   7

Top view of the above binary tree is
4 5 6 7
"""
from collections import deque

from common.problem import Problem


class BottomViewOfBinaryTree(Problem):
    """
    Bottom View of Binary Tree
    """
    PROBLEM_NAME = "BottomViewOfBinaryTree"

    def __init__(self, root_node):
        """Bottom View of Binary Tree

        Args:
            root_node: node of the tree

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.root_node = root_node

    def solve(self):
        """Solve the problem
        Note: O(n) (runtime) solution uses a queue and marks the horizontal distance of the node as it traverses.
              If there is already an element with the same horizontal distance, it overwrites.

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        # A dictionary to store the node's horizontal distance
        node_horizontal_distance_dict = {}

        # A dictionary to store the result
        horizontal_distance_dict = {}

        queue = deque()

        queue.append(self.root_node)
        node_horizontal_distance_dict[self.root_node.data] = 0

        while len(queue) > 0:
            node = queue.popleft()

            # Put the dequeued tree node to Dictionary having key as horizontal distance.
            # Every time we find a node having same horizontal distance we need to replace the data in the map.
            horizontal_distance = node_horizontal_distance_dict[node.data]
            horizontal_distance_dict[horizontal_distance] = node.data

            if node.left is not None:
                node_horizontal_distance_dict[node.left.data] = horizontal_distance - 1
                queue.append(node.left)

            if node.right is not None:
                node_horizontal_distance_dict[node.right.data] = horizontal_distance + 1
                queue.append(node.right)

        bottom_view_list = []

        for it in sorted(horizontal_distance_dict.keys()):
            bottom_view_list.append(horizontal_distance_dict[it])

        return bottom_view_list
