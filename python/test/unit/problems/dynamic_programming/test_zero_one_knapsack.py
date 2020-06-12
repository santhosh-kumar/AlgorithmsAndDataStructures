"""
Unit Test for zero_one_knapsack
"""
from unittest import TestCase

from problems.dynamic_programming.zero_one_knapsack import ZeroOneKnapsack


class TestZeroOneKnapsack(TestCase):
    """
    Unit test for ZeroOneKnapsack
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestZeroOneKnapsack

        Returns:
            None

        Raises:
            None
        """
        # Given
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50

        knapsack_problem = ZeroOneKnapsack(values, weights, capacity)

        # When
        result = knapsack_problem.solve()

        # Then
        self.assertEqual(result, 220)
