"""
Unit Test for longest_increasing_subsequence
"""
from unittest import TestCase

from problems.dynamic_programming.longest_increasing_subsequence import LongestIncreasingSubsequence


class TestLongestIncreasingSubsequence(TestCase):
    """
    Unit test for LongestIncreasingSubsequence
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestLongestIncreasingSubsequence

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

        lis_problem = LongestIncreasingSubsequence(input_list)

        # When
        result = lis_problem.solve()

        # Then
        self.assertEqual(result, 6)
