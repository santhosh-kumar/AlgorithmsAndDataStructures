"""
Unit Test for combination_sum
"""
from unittest import TestCase

from problems.backtracking.combination_sum import CombinationSum


class TestCombinationSum(TestCase):
    """
    Unit test for CombinationSum
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestCombinationSum

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [2, 4, 6, 8]
        target_sum = 8
        combination_sum_problem = CombinationSum(input_list, target_sum)

        # When
        result = combination_sum_problem.solve()

        # Then
        self.assertEqual(result, [[2, 2, 2, 2], [2, 2, 4], [2, 6], [4, 4], [8]])
