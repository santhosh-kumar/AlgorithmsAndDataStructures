"""
Unit Test for two_sum
"""
from unittest import TestCase

from problems.bit_manipulation.count_number_of_bits_to_flip import CountNumberOfBitsToFlip


class TestCountNumberOfBitsToFlip(TestCase):
    """
    Unit test for CountNumberOfBitsToFlip
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestCountNumberOfBitsToFlip

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_number1 = 10
        input_number2 = 20
        count_flip_bits_problem = CountNumberOfBitsToFlip(input_number1, input_number2)

        # When
        result = count_flip_bits_problem.solve()

        # Then
        self.assertEqual(result, 4)
