"""
Unit Test for min_depth_of_binary_tree
"""
from unittest import TestCase

from common.binary_tree import BinaryTreeNode
from problems.binary_tree.min_depth_of_binary_tree_depth_first import MinDepthOfBinaryTreeDepthFirst


class TestMinDepthOfBinaryTreeDepthFirst(TestCase):
    """
    Unit test for MinDepthOfBinaryTreeDepthFirst
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestMinDepthOfBinaryTreeDepthFirst

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

        min_depth_problem = MinDepthOfBinaryTreeDepthFirst(root)

        # When
        depth = min_depth_problem.solve()

        # Then
        self.assertEqual(depth, 2)
