"""
Unit Test for find_kth_smallest_in_unsorted_array
"""
from unittest import TestCase

from problems.array.find_kth_smallest_in_unsorted_array import FindKthSmallestInUnsortedArray


class TestFindKthSmallestInUnsortedArray(TestCase):
    """
    Unit test for FindKthSmallestInUnsortedArray
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestFindKthSmallestInUnsortedArray

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [4, 5, 6, 7, 8, 9, 1, 2, 3]
        find_kth_smallest_problem = FindKthSmallestInUnsortedArray(input_list, 5)

        # When
        smallest = find_kth_smallest_problem.solve()

        # Then
        self.assertEqual(smallest, 5)
