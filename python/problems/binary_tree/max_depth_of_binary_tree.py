"""
Max Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.
"""
from common.problem import Problem


class MaxDepthOfBinaryTree(Problem):
    """
    Max Depth of Binary Tree
    """
    PROBLEM_NAME = "MaxDepthOfBinaryTree"

    def __init__(self, root_node):
        """Max Depth of Binary Tree

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
            Note: O(n) (runtime) and O(log n) (stack space for recursion) solution works by recursively calling maximum depth of left and right subtrees.
            Since the depth of the binary is logn it takes logn space in the stack for recursion.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        return self.max_depth(self.root_node)

    def max_depth(self, root):
        """Find the maximum depth of a binary tree
        Args:
            root: node of the tree

        Returns:
            integer

        Raises:
            None
        """
        if root is None:
            return 0

        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1
