"""
Unit Test for find_min_in_sorted_array
"""
from unittest import TestCase

from problems.array.find_min_in_sorted_rotated_array_with_duplicates import FindMinInSortedRotatedArrayWithDuplicates


class TestFindMinInSortedRotatedArrayWithDuplicates(TestCase):
    """
    Unit test for FindMinInSortedRotatedArrayWithDuplicates
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestFindMinInSortedRotatedArrayWithDuplicates

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [2, 2, 3, 0, 1, 1, 1, 1]
        find_min_problem = FindMinInSortedRotatedArrayWithDuplicates(input_list)

        # When
        min_value = find_min_problem.solve()

        # Then
        self.assertEqual(min_value, 0)
