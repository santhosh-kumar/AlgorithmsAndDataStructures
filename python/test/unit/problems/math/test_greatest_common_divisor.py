"""
Unit Test for reverse_integers
"""
from unittest import TestCase

from problems.math.greatest_common_divisor import GreatestCommonDivisor


class TestGreatestCommonDivisor(TestCase):
    """
    Unit test for GreatestCommonDivisor
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestGreatestCommonDivisor

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_integer1 = 36
        input_integer2 = 24

        gcd_problem = GreatestCommonDivisor(input_integer1, input_integer2)

        # When
        result = gcd_problem.solve()

        # Then
        self.assertEqual(result, 12)
