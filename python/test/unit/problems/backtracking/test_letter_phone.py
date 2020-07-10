"""
Unit Test for letter_phone
"""
from unittest import TestCase

from problems.backtracking.letter_phone import LetterPhone


class TestLetterPhone(TestCase):
    """
    Unit test for LetterPhone
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestLetterPhone

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_integer = 23
        letter_phone_problem = LetterPhone(input_integer)

        # When
        result = letter_phone_problem.solve()

        # Then
        self.assertEqual(result, ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
