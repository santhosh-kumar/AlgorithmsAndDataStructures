"""
Unit Test for longest_substring_with_two_distinct_characters
"""
from unittest import TestCase

from problems.string.longest_substring_with_two_distinct_characters import LongestSubstringWithTwoDistinctCharacters


class TestLongestSubstringWithTwoDistinctCharacters(TestCase):
    """
    Unit test for TestLongestSubstringWithTwoDistinctCharacters
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestLongestSubstringWithTwoDistinctCharacters

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "abaac"
        longest_substring_problem = LongestSubstringWithTwoDistinctCharacters(input_string)

        # When
        result = longest_substring_problem.solve()

        # Then
        self.assertEqual(result, 4)
