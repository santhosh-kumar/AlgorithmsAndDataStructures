"""
Unit Test for longest_substring_without_repeating_characters
"""
from unittest import TestCase

from problems.string.longest_substring_without_repeating_characters import LongestSubstringWithoutRepeatingCharacters


class TestLongestSubstringWithoutRepeatingCharacters(TestCase):
    """
    Unit test for TestLongestSubstringWithoutRepeatingCharacters
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestLongestSubstringWithoutRepeatingCharacters

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "abcabcbb"
        longest_substring_problem = LongestSubstringWithoutRepeatingCharacters(input_string)

        # When
        result = longest_substring_problem.solve()

        # Then
        self.assertEqual(result, 3)

    def test_solve_in_the_middle(self):
        """Test solve (in the middle of the string)

        Args:
            self: TestLongestSubstringWithoutRepeatingCharacters

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "pwwkew"
        longest_substring_problem = LongestSubstringWithoutRepeatingCharacters(input_string)

    def test_solve_repeated(self):
        """Test solve (repeated characters)

        Args:
            self: TestLongestSubstringWithoutRepeatingCharacters

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "bbbbbb"
        longest_substring_problem = LongestSubstringWithoutRepeatingCharacters(input_string)

        # When
        result = longest_substring_problem.solve()

        # Then
        self.assertEqual(result, 1)
