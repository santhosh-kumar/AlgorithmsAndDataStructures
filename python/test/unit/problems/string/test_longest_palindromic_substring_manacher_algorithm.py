"""
Unit Test for longest_palindromic_substring_manacher_algorithm
"""
from unittest import TestCase

from problems.string.longest_palindromic_substring_manacher_algorithm import \
    LongestPalindromicSubstringManacherAlgorithm


class TestLongestPalindromicSubstringManacherAlgorithm(TestCase):
    """
    Unit test for LongestPalindromicSubstringManacherAlgorithm
    """

    def test_solve(self):
        """Test solve (success)

        Args:
            self: TestLongestPalindromicSubstringManacherAlgorithm

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "abac"
        longest_palindromic_problem = LongestPalindromicSubstringManacherAlgorithm(input_string)

        # When
        palindromic_string = longest_palindromic_problem.solve()

        # Then
        self.assertEqual(palindromic_string, "aba")
