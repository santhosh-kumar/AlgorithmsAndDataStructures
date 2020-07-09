"""
Unit Test for find_triplets_with_zero_sum
"""
from unittest import TestCase

from problems.array.find_triplets_with_zero_sum import FindTripletsWithZeroSum


class TestFindTripletsWithZeroSum(TestCase):
    """
    Unit test for FindTripletsWithZeroSum
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestFindTripletsWithZeroSum

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [0, -1, 2, -3, 1]

        triplets_problem = FindTripletsWithZeroSum(input_list)

        # When
        result = triplets_problem.solve()

        # Then
        self.assertEqual(result, [[-3, 1, 2], [-1, 0, 1]])
