"""
Unit Test for roman_to_integer
"""
from unittest import TestCase

from problems.misc.roman_to_integer import RomanToInteger


class TestRomanToInteger(TestCase):
    """
    Unit test for RomanToInteger
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestRomanToInteger

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_roman_numerals = "MMMCMXCIX"
        roman_to_integer_problem = RomanToInteger(input_roman_numerals)

        # When
        integer_result = roman_to_integer_problem.solve()

        # Then
        self.assertEqual(integer_result, 3999)
