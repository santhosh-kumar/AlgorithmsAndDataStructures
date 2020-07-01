"""
Unit Test for binary_tree_upside_down
"""
from unittest import TestCase

from common.binary_tree import BinaryTreeNode
from problems.binary_tree.binary_tree_upside_down import BinaryTreeUpsideDown


class TestBinaryTreeUpsideDown(TestCase):
    """
    Unit test for BinaryTreeUpsideDown
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestBinaryTreeUpsideDown

        Returns:
            None

        Raises:
            None
        """
        # Given
        root = BinaryTreeNode(1)
        root.left = BinaryTreeNode(2)

        root.left.left = BinaryTreeNode(4)
        root.left.right = BinaryTreeNode(5)
        root.right = BinaryTreeNode(3)

        upside_down_problem = BinaryTreeUpsideDown(root)

        # When
        node = upside_down_problem.solve()

        # Then
        elements_list = []
        BinaryTreeNode.in_order(node, elements_list)
        self.assertEqual(elements_list, [5, 4, 3, 2, 1])
