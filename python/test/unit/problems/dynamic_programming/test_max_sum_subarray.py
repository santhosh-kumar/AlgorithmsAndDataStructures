"""
Unit Test for max_sum_subarray
"""
from unittest import TestCase

from problems.dynamic_programming.max_sum_subarray import MaxSumSubArray


class TestMaxSumSubArray(TestCase):
    """
    Unit test for MaxSumSubArray
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestMaxSumSubArray

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [2, 1, -3, 4, -1, 2, 1, -5, 4]

        max_sum_subarray_problem = MaxSumSubArray(input_list)

        # When
        result = max_sum_subarray_problem.solve()

        # Then
        self.assertEqual(result, 6)
