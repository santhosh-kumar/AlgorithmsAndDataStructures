"""
Unit Test for two_sum
"""
from unittest import TestCase

from problems.array.two_sum import TwoSum


class TestTwoSum(TestCase):
    """
    Unit test for TwoSum
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestTwoSum

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [2, 6, 7, 5, 8, 9]
        target_sum = 7
        two_sum_problem = TwoSum(input_list, target_sum)

        # When
        indices = two_sum_problem.solve()

        # Then
        self.assertEqual(indices, (1, 4))
