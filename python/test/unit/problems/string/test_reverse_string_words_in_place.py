"""
Unit Test for reverse_string_words_in_place
"""
from unittest import TestCase

from problems.string.reverse_string_words_in_place import ReverseStringWordsInPlace


class TestReverseStringWordsInPlace(TestCase):
    """
    Unit test for ReverseStringWordsInPlace
    """

    def test_solve(self):
        """Test solve (in place)

        Args:
            self: ReverseStringWordsInPlace

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
