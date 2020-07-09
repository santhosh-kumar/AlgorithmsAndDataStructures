"""
Unit Test for find_nth_fibanacci_number
"""
from unittest import TestCase

from problems.dynamic_programming.find_nth_fibanacci_number import FindNthFibanacciNumber


class TestFindNthFibanacciNumber(TestCase):
    """
    Unit test for FindNthFibanacciNumber
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestFindNthFibanacciNumber

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_integer = 9
        nth_fibanacci_problem = FindNthFibanacciNumber(input_integer)

        # When
        result = nth_fibanacci_problem.solve()

        # Then
        self.assertEqual(result, 34)
