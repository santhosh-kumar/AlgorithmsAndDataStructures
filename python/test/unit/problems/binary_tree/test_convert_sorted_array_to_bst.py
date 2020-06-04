"""
Unit Test for convert_sorted_array_to_bst
"""
from unittest import TestCase

from common.linked_list import BinaryTreeNode
from problems.binary_tree.convert_sorted_array_to_bst import ConvertSortedArrayToBST


class TestConvertSortedArrayToBST(TestCase):
    """
    Unit test for ConvertSortedArrayToBST
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestConvertSortedArrayToBST

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [range(1, 10)]
        covert_to_bst_problem = ConvertSortedArrayToBST(input_list)

        # When
        node = covert_to_bst_problem.solve()

        # in order traversal returns the binary search tree in sorted order
        in_order_result = []
        BinaryTreeNode.in_order(node, in_order_result)

        # Then
        self.assertEqual(in_order_result, input_list)
