"""
Unit Test for two_sum_sorted
"""
from unittest import TestCase

from problems.array.two_sum_sorted import TwoSumSorted


class TestTwoSumSorted(TestCase):
    """
    Unit test for TwoSumSorted
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TwoSumSorted

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [2, 3, 7, 9, 12]
        target_sum = 16
        two_sum_problem = TwoSumSorted(input_list, target_sum)

        # When
        indices = two_sum_problem.solve()

        # Then
        self.assertEqual(indices, (3, 4))
