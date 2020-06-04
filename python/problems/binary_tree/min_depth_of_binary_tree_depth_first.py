"""
Min Depth of Binary Tree (Depth First)

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
from common.problem import Problem


class MinDepthOfBinaryTreeDepthFirst(Problem):
    """
    Min Depth of Binary Tree (Depth First)
    """
    PROBLEM_NAME = "MinDepthOfBinaryTreeDepthFirst"

    def __init__(self, root_node):
        """Min Depth of Binary Tree (Depth First)

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
            Note:

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        return self.min_depth(self.root_node)

    def min_depth(self, root):
        """Find the minimum depth of a binary tree
        Args:
            root: node of the tree

        Returns:
            integer

        Raises:
            None
        """
        if root is None:
            return 0
        if root.left is None:
            return self.min_depth(root.right) + 1
        if root.right is None:
            return self.min_depth(root.left) + 1

        return min(self.min_depth(root.left), self.min_depth(root.right)) + 1
