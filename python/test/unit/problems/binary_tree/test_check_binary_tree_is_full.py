"""
Unit Test for check_binary_tree_is_full
"""
from unittest import TestCase

from common.linked_list import BinaryTreeNode
from problems.binary_tree.check_binary_tree_is_full import CheckBinaryTreeIsFull


class TestCheckBinaryTreeIsFull(TestCase):
    """
    Unit test for CheckBinaryTreeIsFull
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestCheckBinaryTreeIsFull

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

        full_tree_problem = CheckBinaryTreeIsFull(root)

        # Then
        self.assertTrue(full_tree_problem.solve())

    def test_solve_invalid(self):
        """Test solve (invalid)

        Args:
            self: TestCheckBinaryTreeIsFull

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
        # root.right.right.left = BinaryTreeNode(6)

        full_tree_problem = CheckBinaryTreeIsFull(root)

        # Then
        self.assertFalse(full_tree_problem.solve())
