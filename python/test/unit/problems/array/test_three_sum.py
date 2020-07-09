"""
Unit Test for three_sum
"""
from unittest import TestCase

from problems.array.three_sum import ThreeSum


class TestThreeSum(TestCase):
    """
    Unit test for ThreeSum
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestThreeSum

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [-1, 2, 1, -4]
        target_sum = 1
        three_sum_problem = ThreeSum(input_list, target_sum)

        # When
        result = three_sum_problem.solve()

        # Then
        self.assertEqual(result, 2)
