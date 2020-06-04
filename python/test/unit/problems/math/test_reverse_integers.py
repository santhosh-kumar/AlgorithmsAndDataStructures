"""
Unit Test for reverse_integers
"""
from unittest import TestCase

from problems.math.reverse_integers import ReverseIntegers


class TestReverseIntegers(TestCase):
    """
    Unit test for ReverseIntegers
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestReverseIntegers

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_integer = 123
        reverse_integers_problem = ReverseIntegers(input_integer)

        # When
        result = reverse_integers_problem.solve()

        # Then
        self.assertEqual(result, 321)

    def test_solve_negative(self):
        """Test solve (negative)

        Args:
            self: TestReverseIntegers

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_integer = -123
        reverse_integers_problem = ReverseIntegers(input_integer)

        # When
        result = reverse_integers_problem.solve()

        # Then
        self.assertEqual(result, -321)

    def test_solve_overflow(self):
        """Test solve (overflow)

        Args:
            self: TestReverseIntegers

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_integer = 1000000003
        reverse_integers_problem = ReverseIntegers(input_integer)

        # When
        result = reverse_integers_problem.solve()

        # Then
        self.assertEqual(result, 0)
