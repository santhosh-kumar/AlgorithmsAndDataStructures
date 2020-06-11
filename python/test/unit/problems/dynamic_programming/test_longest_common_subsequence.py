"""
Unit Test for LongestCommonSubsequence
"""
from unittest import TestCase

from problems.dynamic_programming.longest_common_subsequence import LongestCommonSubsequence


class TestLongestCommonSubsequence(TestCase):
    """
    Unit test for LongestCommonSubsequence
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestLongestCommonSubsequence

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string1 = "AGGTAB"
        input_string2 = "GXTXAYB"
        lcs_problem = LongestCommonSubsequence(input_string1, input_string2)

        # When
        result = lcs_problem.solve()

        # Then
        self.assertEqual(result, 4)
