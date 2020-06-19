"""
Unit Test for two_sum
"""
from unittest import TestCase

from problems.array.merge_intervals import MergeIntervals


class TestMergeIntervals(TestCase):
    """
    Unit test for MergeIntervals
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestMergeIntervals

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_range_list1 = [[1, 9], [19, 20], [0, 3], [0, 1]]
        input_range_list2 = [[2, 5], [10, 11], [12, 20], [0, 2]]
        merge_intervals_problem = MergeIntervals(input_range_list1, input_range_list2)

        # When
        result = merge_intervals_problem.solve()

        # Then
        self.assertEqual(result, [[0, 9], [10, 11], [12, 20]])
