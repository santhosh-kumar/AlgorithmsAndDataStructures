"""
Unit Test for palindrome_number
"""
from unittest import TestCase

from problems.math.palindrome_number import PalindromeNumber


class TestPalindromeNumber(TestCase):
    """
    Unit test for PalindromeNumber
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestPalindromeNumber

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = 1234321
        palindrome_number_problem = PalindromeNumber(input_string)

        # Then
        self.assertTrue(palindrome_number_problem.solve())

    def test_solve_negative(self):
        """Test solve (negative)

        Args:
            self: TestPalindromeNumber

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = -1234321
        palindrome_number_problem = PalindromeNumber(input_string)

        # Then
        self.assertFalse(palindrome_number_problem.solve())
