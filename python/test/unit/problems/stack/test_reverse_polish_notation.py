"""
Unit Test for reverse_polish_notation
"""
from unittest import TestCase

from problems.stack.reverse_polish_notation import ReversePolishNotation


class TestReversePolishNotation(TestCase):
    """
    Unit test for ReversePolishNotation
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestReversePolishNotation

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = ["2", "1", "+", "3", "*"]
        reverse_polish_problem = ReversePolishNotation(input_list)

        # When
        result = reverse_polish_problem.solve()

        # Then
        self.assertEqual(result, 9)
