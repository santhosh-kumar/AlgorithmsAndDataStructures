"""
Unit Test for decode_digit_sequence
"""
from unittest import TestCase

from problems.dynamic_programming.decode_digit_sequence import DecodeDigitSequence


class TestDecodeDigitSequence(TestCase):
    """
    Unit test for DecodeDigitSequence
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestDecodeDigitSequence

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "1234"
        decode_problem = DecodeDigitSequence(input_string)

        # When
        result = decode_problem.solve()

        # Then
        self.assertEqual(result, 3)
