"""
Unit Test for valid_palindrome
"""
from unittest import TestCase

from problems.string.valid_palindrome import ValidPalindrome


class TestValidPalindrome(TestCase):
    """
    Unit test for ValidPalindrome
    """

    def test_is_letter_or_digit(self):
        """is_letter_or_digit

        Args:
            self: TestValidPalindrome

        Returns:
            None

        Raises:
            None
        """
        self.assertTrue(ValidPalindrome.is_letter_or_digit("a"))
        self.assertTrue(ValidPalindrome.is_letter_or_digit("1"))
        self.assertFalse(ValidPalindrome.is_letter_or_digit(","))
        self.assertFalse(ValidPalindrome.is_letter_or_digit(" "))
        self.assertFalse(ValidPalindrome.is_letter_or_digit("%"))

    def test_solve_success(self):
        """Test solve (success)

        Args:
            self: TestValidPalindrome

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "A man, a plan, a canal: Panama"
        valid_palindrome_problem = ValidPalindrome(input_string)

        # Then
        self.assertTrue(valid_palindrome_problem.solve())

    def test_solve_failed(self):
        """Test solve (failed)

        Args:
            self: TestValidPalindrome

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "race a car"
        valid_palindrome_problem = ValidPalindrome(input_string)

        # Then
        self.assertFalse(valid_palindrome_problem.solve())
