"""
Unit Test for single_number
"""
from unittest import TestCase

from problems.bit_manipulation.single_number_thrice import SingleNumberThrice


class TestSingleNumberThrice(TestCase):
    """
    Unit test for SingleNumberThrice
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestSingleNumberThrice

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [1, 1, 1, 2, 2, 2, 3, 3, 4, 3]
        single_number_problem = SingleNumberThrice(input_list)

        # When
        single_number = single_number_problem.solve()

        # Then
        self.assertEqual(single_number, 4)
