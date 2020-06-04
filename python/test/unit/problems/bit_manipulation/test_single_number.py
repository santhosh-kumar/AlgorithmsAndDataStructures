"""
Unit Test for single_number
"""
from unittest import TestCase

from problems.bit_manipulation.single_number import SingleNumber


class TestSingleNumber(TestCase):
    """
    Unit test for SingleNumber
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestSingleNumber

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [1, 2, 1, 3, 3, 4, 4, 5, 5, 2, 6, 6, 7, 8, 8]
        single_number_problem = SingleNumber(input_list)

        # When
        single_number = single_number_problem.solve()

        # Then
        self.assertEqual(single_number, 7)
