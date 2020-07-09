"""
Unit Test for square_root
"""
from unittest import TestCase

from problems.math.square_root import SquareRoot


class TestSquareRoot(TestCase):
    """
    Unit test for SquareRoot
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestSquareRoot

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_integer = 11
        square_root_problem = SquareRoot(input_integer)

        # When
        result = square_root_problem.solve()

        # Then
        self.assertEqual(result, 3)
