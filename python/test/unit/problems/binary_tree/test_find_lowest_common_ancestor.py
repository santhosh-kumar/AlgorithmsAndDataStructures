"""
Unit Test for max_depth_of_binary_tree
"""
from unittest import TestCase

from common.linked_list import BinaryTreeNode
from problems.binary_tree.find_lowest_common_ancestor import FindLowestCommonAncestor


class TestFindLowestCommonAncestor(TestCase):
    """
    Unit test for FindLowestCommonAncestor
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestFindLowestCommonAncestor

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

        lca_problem = FindLowestCommonAncestor(root, 2, 6)

        # When
        result = lca_problem.solve()

        # Then
        self.assertEqual(result.data, 3)
