"""
Unit Test for integer_to_roman
"""
from unittest import TestCase

from problems.misc.integer_to_roman import IntegerToRoman


class TestIntegerToRoman(TestCase):
    """
    Unit test for IntegerToRoman
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestIntegerToRoman

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = 3999
        integer_to_roman_problem = IntegerToRoman(input_string)

        # When
        roman_numerals = integer_to_roman_problem.solve()

        # Then
        self.assertEqual(roman_numerals, "MMMCMXCIX")
