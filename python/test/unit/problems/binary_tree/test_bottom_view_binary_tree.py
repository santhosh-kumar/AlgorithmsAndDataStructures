"""
Unit Test for bottom_view_binary_tree
"""
from unittest import TestCase

from common.binary_tree import BinaryTreeNode
from problems.binary_tree.bottom_view_binary_tree import BottomViewOfBinaryTree


class TestBottomViewOfBinaryTree(TestCase):
    """
    Unit test for BottomViewOfBinaryTree
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestBottomViewOfBinaryTree

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

        bottom_view_problem = BottomViewOfBinaryTree(root)

        # When
        result = bottom_view_problem.solve()

        # Then
        self.assertEqual(result, [2, 4, 6, 7, 8])
