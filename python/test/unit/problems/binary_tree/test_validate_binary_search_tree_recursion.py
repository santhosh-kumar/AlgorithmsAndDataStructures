"""
Unit Test for validate_binary_search_tree_recursion
"""
from unittest import TestCase

from common.binary_tree import BinaryTreeNode
from problems.binary_tree.validate_binary_search_tree_recursion import ValidateBinarySearchTreeRecursion


class TestValidateBinarySearchTreeRecursion(TestCase):
    """
    Unit test for ValidateBinarySearchTreeRecursion
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestValidateBinarySearchTreeRecursion

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

        validate_binary_search_tree_problem = ValidateBinarySearchTreeRecursion(root)

        # When
        is_valid = validate_binary_search_tree_problem.solve()

        # Then
        self.assertTrue(is_valid)

    def test_solve_in_valid(self):
        """Test solve (in valid)

        Args:
            self: TestValidateBinarySearchTreeRecursion

        Returns:
            None

        Raises:
            None
        """
        # Given
        root = BinaryTreeNode(3)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(5)
        root.right.left = BinaryTreeNode(1)  # should be greater than 3
        root.right.right = BinaryTreeNode(7)

        validate_binary_search_tree_problem = ValidateBinarySearchTreeRecursion(root)

        # When
        is_valid = validate_binary_search_tree_problem.solve()

        # Then
        self.assertFalse(is_valid)
