"""
Unit Test for reverse_string_words
"""
from unittest import TestCase

from problems.string.reverse_string_words import ReverseStringWords
from problems.string.reverse_string_words_in_place import ReverseStringWordsInPlace


class TestReverseStringWords(TestCase):
    """
    Unit test for ReverseStringWords
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestReverseStringWords

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "the sky is blue"
        reverse_string_words_problem = ReverseStringWords(input_string)

        # When
        revered_string = reverse_string_words_problem.solve()

        # Then
        self.assertEqual(revered_string, "blue is sky the")

    def test_solve_in_place(self):
        """Test solve (in place)

        Args:
            self: TestReverseStringWords

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "the sky is blue"
        reverse_string_words_in_place_problem = ReverseStringWordsInPlace(input_string)

        # When
        revered_string = reverse_string_words_in_place_problem.solve()

        # Then
        self.assertEqual(revered_string, "blue is sky the")
