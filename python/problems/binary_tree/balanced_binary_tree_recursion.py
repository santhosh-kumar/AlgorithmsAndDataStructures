"""
Balanced Binary Tree (Recursion)

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the
depth of the two subtrees of every node never differs by more than 1.
"""
from common.problem import Problem


class BalancedBinaryTreeRecursion(Problem):
    """
    Balanced Binary Tree (Recursion)
    """
    PROBLEM_NAME = "BalancedBinaryTreeRecursion"

    def __init__(self, root_node):
        """Balanced Binary Tree (Recursion)

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
        Note: O(n) (runtime) and O(n) (stack space) solution works by checking is the subtree is balanced at each step.
        Otherwise, -1 is returned.

        Args:

        Returns:
            None

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        return self.is_balanced(self.root_node)

    def is_balanced(self, root):
        """Check if the binary tree is balanced

        Args:
            root: node of the tree

        Returns:
            boolean

        Raises:
            None
        """
        return self.max_depth(root) != -1

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

        left_depth = self.max_depth(root.left)
        if left_depth == -1:
            return -1

        right_depth = self.max_depth(root.right)
        if right_depth == -1:
            return -1

        if abs(left_depth - right_depth) <= 1:
            return max(left_depth, right_depth) + 1
        else:
            return -1
