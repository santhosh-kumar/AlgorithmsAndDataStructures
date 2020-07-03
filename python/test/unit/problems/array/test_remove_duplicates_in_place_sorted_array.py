"""
Unit Test for remove_duplicates_in_place_sorted_array
"""
from unittest import TestCase

from problems.array.remove_duplicates_in_place_sorted_array import RemoveDuplicatesInPlaceSortedArray


class TestRemoveDuplicatesInPlaceSortedArray(TestCase):
    """
    Unit test for RemoveDuplicatesInPlaceSortedArray
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestRemoveDuplicatesInPlaceSortedArray

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 6, 6, 6, 7, 7]
        two_sum_problem = RemoveDuplicatesInPlaceSortedArray(input_list)

        # When
        result = two_sum_problem.solve()

        # Then
        self.assertEqual(result, 6)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], input_list[:result + 1])

    def test_solve_no_duplicate(self):
        """Test solve

        Args:
            self: TestRemoveDuplicatesInPlaceSortedArray

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [1, 2, 3, 4, 5, 6, 7, 8]
        two_sum_problem = RemoveDuplicatesInPlaceSortedArray(input_list)

        # When
        result = two_sum_problem.solve()

        # Then
        self.assertEqual(result, 7)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], input_list[:result + 1])
