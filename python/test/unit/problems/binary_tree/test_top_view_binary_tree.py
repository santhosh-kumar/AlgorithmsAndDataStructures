"""
Unit Test for min_depth_of_binary_tree
"""
from unittest import TestCase

from common.linked_list import BinaryTreeNode
from problems.binary_tree.top_view_binary_tree import TopViewOfBinaryTree


class TestTopViewOfBinaryTree(TestCase):
    """
    Unit test for TopViewOfBinaryTree
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestTopViewOfBinaryTree

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

        top_view_problem = TopViewOfBinaryTree(root)

        # When
        result = top_view_problem.solve()

        # Then
        self.assertEqual(result, [2, 3, 5, 7, 8])
