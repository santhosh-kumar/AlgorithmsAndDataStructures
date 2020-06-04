"""
Unit Test for max_product_subarray
"""
from unittest import TestCase

from problems.dynamic_programming.max_product_subarray import MaxProductSubArray


class TestMaxProductSubArray(TestCase):
    """
    Unit test for MaxProductSubArray
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestMaxProductSubArray

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [2, 3, -2, 4]

        max_product_subarray_problem = MaxProductSubArray(input_list)

        # When
        result = max_product_subarray_problem.solve()

        # Then
        self.assertEqual(result, 6)
