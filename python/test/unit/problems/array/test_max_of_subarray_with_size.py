"""
Unit Test for max_of_subarray_with_size
"""
from unittest import TestCase

from problems.array.max_of_subarray_with_size import MaxOfSubArrayWithSize


class TestMaxOfSubArrayWithSize(TestCase):
    """
    Unit test for MaxOfSubArrayWithSize
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestMaxOfSubArrayWithSize

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [2, 6, 7, 5, 8, 9]
        size = 3
        max_subarray_problem = MaxOfSubArrayWithSize(input_list, 3)

        # When
        result = max_subarray_problem.solve()

        # Then
        self.assertEqual(result, 22)
