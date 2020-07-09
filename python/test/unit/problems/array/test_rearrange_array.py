"""
Unit Test for rearrange_array
"""
from unittest import TestCase

from problems.array.rearrange_array import RearrangeArray


class TestRearrangeArray(TestCase):
    """
    Unit test for RearrangeArray
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestRearrangeArray

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [4, 0, 2, 1, 3]
        rearrange_array_problem = RearrangeArray(input_list)

        # When
        result = rearrange_array_problem.solve()

        # Then
        self.assertEqual(result, [3, 4, 2, 0, 1])
