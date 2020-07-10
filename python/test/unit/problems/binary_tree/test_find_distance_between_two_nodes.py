"""
Unit Test for find_distance_between_two_nodes
"""
from unittest import TestCase

from common.binary_tree import BinaryTreeNode
from problems.binary_tree.find_distance_between_two_nodes import FindDistanceBetweenTwoNodes


class TestFindDistanceBetweenTwoNodes(TestCase):
    """
    Unit test for FindDistanceBetweenTwoNodes
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestFindDistanceBetweenTwoNodes

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

        distance_problem = FindDistanceBetweenTwoNodes(root, 2, 6)

        # When
        result = distance_problem.solve()

        # Then
        self.assertEqual(result, 4)
