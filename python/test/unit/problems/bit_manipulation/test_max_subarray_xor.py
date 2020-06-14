"""
Unit Test for two_sum
"""
from unittest import TestCase

from problems.bit_manipulation.max_subarray_xor import MaxSubarrayXOR


class TestMaxSubarrayXOR(TestCase):
    """
    Unit test for MaxSubarrayXOR
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestMaxSubarrayXOR

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [8, 1, 2, 12, 7, 6]
        max_subarray_xor_problem = MaxSubarrayXOR(input_list)

        # When
        result = max_subarray_xor_problem.solve()

        # Then
        self.assertEqual(result, 15)
