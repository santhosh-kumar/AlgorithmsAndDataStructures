"""
Unit Test for max_depth_of_binary_tree
"""
from unittest import TestCase

from common.linked_list import BinaryTreeNode
from problems.binary_tree.max_depth_of_binary_tree import MaxDepthOfBinaryTree


class TestMaxDepthOfBinaryTree(TestCase):
    """
    Unit test for MaxDepthOfBinaryTree
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestMaxDepthOfBinaryTree

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

        max_depth_problem = MaxDepthOfBinaryTree(root)

        # When
        depth = max_depth_problem.solve()

        # Then
        self.assertEqual(depth, 4)
