"""
Top View of Binary Tree

Top view of a binary tree is the set of nodes visible when the tree is viewed from the top.
Given a binary tree, print the top view of it. The output nodes can be printed in any order.

For example:

       1
    /     \
   2       3
  /  \    / \
 4    5  6   7

Top view of the above binary tree is
4 2 1 3 7
"""
from common.problem import Problem


class TopViewOfBinaryTree(Problem):
    """
    Top View of Binary Tree
    """
    PROBLEM_NAME = "TopViewOfBinaryTree"

    def __init__(self, root_node):
        """Top View of Binary Tree

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
        Note: O(n) (runtime) solution uses a map to record the data and level of nodes. If there is a node already at a data,
        it will be updated if it's at a higher level.

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        # A dictionary to store the node and it's level from the root
        level_dict = {}

        self.fill_level(self.root_node, 0, 0, level_dict)

        top_view_list = []

        for it in sorted(level_dict.keys()):
            top_view_list.append(level_dict[it][0])

        return top_view_list

    def fill_level(self, root, distance, level, level_dict):
        """Fill the level
        Args:

        Returns:
            integer

        Raises:
            None
        """
        if root is None:
            return

        if distance not in level_dict:
            level_dict[distance] = [root.data, level]
        elif level_dict[distance][1] > level:
            level_dict[distance] = [root.data, level]

        self.fill_level(root.left, distance - 1, level + 1, level_dict)

        self.fill_level(root.right, distance + 1, level + 1, level_dict)
