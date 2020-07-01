"""
Unit Test for balanced_binary_tree_brute_force
"""
from unittest import TestCase

from common.binary_tree import BinaryTreeNode
from problems.binary_tree.balanced_binary_tree_brute_force import BalancedBinaryTreeBruteForce


class TestBalancedBinaryTreeBruteForce(TestCase):
    """
    Unit test for BalancedBinaryTreeBruteForce
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestBalancedBinaryTreeBruteForce

        Returns:
            None

        Raises:
            None
        """
        # Given
        root = BinaryTreeNode(3)
        root.left = BinaryTreeNode(2)

        root.left.left = BinaryTreeNode(1)
        root.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(4)
        root.right.right = BinaryTreeNode(7)

        balanced_tree_problem = BalancedBinaryTreeBruteForce(root)

        # When
        is_balanced = balanced_tree_problem.solve()

        # Then
        self.assertTrue(is_balanced)

    def test_solve_not_balanced(self):
        """Test solve (Not Balanced)

        Args:
            self: TestBalancedBinaryTreeBruteForce

        Returns:
            None

        Raises:
            None
        """
        # Given
        root = BinaryTreeNode(3)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(4)
        root.right.right = BinaryTreeNode(7)
        root.right.right.right = BinaryTreeNode(8)
        root.right.right.left = BinaryTreeNode(6)

        balanced_tree_problem = BalancedBinaryTreeBruteForce(root)

        # When
        is_balanced = balanced_tree_problem.solve()

        # Then
        self.assertFalse(is_balanced)
