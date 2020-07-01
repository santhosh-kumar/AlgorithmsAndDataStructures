"""
Unit Test for right_view_binary_tree
"""
from unittest import TestCase

from common.binary_tree import BinaryTreeNode
from problems.binary_tree.right_view_binary_tree import RightViewOfBinaryTree


class TestRightViewOfBinaryTree(TestCase):
    """
    Unit test for RightViewOfBinaryTree
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestRightViewOfBinaryTree

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

        right_view_problem = RightViewOfBinaryTree(root)

        # When
        result = right_view_problem.solve()

        # Then
        self.assertEqual(result, [3, 5, 7, 8])
