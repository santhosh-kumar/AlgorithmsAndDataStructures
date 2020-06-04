"""
Unit Test for longest_palindromic_substring
"""
from unittest import TestCase

from problems.string.longest_palindromic_substring import LongestPalindromicSubstring


class TestLongestPalindromicSubstring(TestCase):
    """
    Unit test for LongestPalindromicSubstring
    """

    def test_solve(self):
        """Test solve (success)

        Args:
            self: TestLongestPalindromicSubstring

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "abac"
        longest_palindromic_problem = LongestPalindromicSubstring(input_string)

        # When
        palindromic_string = longest_palindromic_problem.solve()

        # Then
        self.assertEqual(palindromic_string, "aba")
