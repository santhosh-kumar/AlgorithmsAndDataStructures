"""
Unit Test for check_binary_tree_is_subtree
"""
from unittest import TestCase

from common.binary_tree import BinaryTreeNode
from problems.binary_tree.check_binary_tree_is_subtree import CheckBinaryTreeIsSubtree


class TestCheckBinaryTreeIsSubtree(TestCase):
    """
    Unit test for CheckBinaryTreeIsSubtree
    """

    def test_solve(self):
        """Test solve

        Args:
            self: CheckBinaryTreeIsSubtree

        Returns:
            None

        Raises:
            None
        """
        # Given
        root1 = BinaryTreeNode(3)
        root1.left = BinaryTreeNode(2)
        root1.right = BinaryTreeNode(5)
        root1.right.left = BinaryTreeNode(4)
        root1.right.right = BinaryTreeNode(7)
        root1.right.right.right = BinaryTreeNode(8)
        root1.right.right.left = BinaryTreeNode(6)

        root2 = BinaryTreeNode(5)
        root2.left = BinaryTreeNode(4)
        root2.right = BinaryTreeNode(7)
        root2.right.right = BinaryTreeNode(8)
        root2.right.left = BinaryTreeNode(6)

        sub_tree_problem = CheckBinaryTreeIsSubtree(root1, root2)

        # Then
        self.assertTrue(sub_tree_problem.solve())

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
        root1 = BinaryTreeNode(3)
        root1.left = BinaryTreeNode(2)
        root1.right = BinaryTreeNode(5)
        root1.right.left = BinaryTreeNode(4)
        root1.right.right = BinaryTreeNode(7)
        root1.right.right.right = BinaryTreeNode(8)
        root1.right.right.left = BinaryTreeNode(6)

        root2 = BinaryTreeNode(5)
        root2.left = BinaryTreeNode(4)
        root2.right = BinaryTreeNode(7)
        root2.right.right = BinaryTreeNode(8)

        sub_tree_problem = CheckBinaryTreeIsSubtree(root1, root2)

        # Then
        self.assertFalse(sub_tree_problem.solve())
