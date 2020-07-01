"""
Unit Test for binary_tree_max_sum_path
"""
from unittest import TestCase

from common.binary_tree import BinaryTreeNode
from problems.binary_tree.binary_tree_max_sum_path import BinaryTreeMaxSumPath


class TestBinaryTreeMaxSumPath(TestCase):
    """
    Unit test for BinaryTreeMaxSumPath
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestBinaryTreeMaxSumPath

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

        max_sum_path_problem = BinaryTreeMaxSumPath(root)

        # When
        max_sum = max_sum_path_problem.solve()

        # Then
        self.assertEqual(max_sum, 18)
