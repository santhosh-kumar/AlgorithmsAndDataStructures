"""
Unit Test for convert_sorted_array_to_bst
"""
from unittest import TestCase

from problems.binary_tree.check_array_is_preorder_bst import CheckArrayIsPreOrderBST


class TestCheckArrayIsPreOrderBST(TestCase):
    """
    Unit test for CheckArrayIsPreOrderBST
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestCheckArrayIsPreOrderBST

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [5, 3, 2, 4, 7, 6, 8]
        array_preorder_bst_problem = CheckArrayIsPreOrderBST(input_list)

        # When
        self.assertTrue(array_preorder_bst_problem.solve())

    def test_solve_invalid(self):
        """Test solve (invalid)

        Args:
            self: TestCheckArrayIsPreOrderBST

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [5, 6, 2, 4, 7, 6, 8]
        array_preorder_bst_problem = CheckArrayIsPreOrderBST(input_list)

        # When
        self.assertFalse(array_preorder_bst_problem.solve())
