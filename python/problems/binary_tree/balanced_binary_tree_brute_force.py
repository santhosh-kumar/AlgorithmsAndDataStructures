"""
Balanced Binary Tree (Brute Force)

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the
depth of the two subtrees of every node never differs by more than 1.
"""
from common.problem import Problem


class BalancedBinaryTreeBruteForce(Problem):
    """
    Balanced Binary Tree (Brute Force)
    """
    PROBLEM_NAME = "BalancedBinaryTreeBruteForce"

    def __init__(self, root_node):
        """Balanced Binary Tree (Brute Force)

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

        Note: O(n^2) (runtime) and O(n) (stack space) solution recursively calculates the maximum depth of the tree of left and right nodes.
        Then verifies that the depth of the left and right subtrees should differ at max by 1.

        Args:

        Returns:
            boolean

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
        if root is None:
            return True

        return (abs(self.max_depth(root.left) - self.max_depth(root.right)) <= 1) and self.is_balanced(
            root.left) and self.is_balanced(root.right)

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
