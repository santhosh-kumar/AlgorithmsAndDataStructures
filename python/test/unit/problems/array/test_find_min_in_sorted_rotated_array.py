"""
Unit Test for find_min_in_sorted_array
"""
from unittest import TestCase

from problems.array.find_min_in_sorted_rotated_array import FindMinInSortedRotatedArray


class TestFindMinInSortedRotatedArray(TestCase):
    """
    Unit test for FindMinInSortedRotatedArray
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestFindMinInSortedRotatedArray

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [4, 5, 6, 7, 8, 9, 1, 2, 3]
        find_min_problem = FindMinInSortedRotatedArray(input_list)

        # When
        min_value = find_min_problem.solve()

        # Then
        self.assertEqual(min_value, 1)
