"""
Unit Test for add_two_binary_strings
"""
from unittest import TestCase

from problems.string.add_two_binary_strings import AddTwoBinaryStrings


class TestAddTwoBinaryStrings(TestCase):
    """
    Unit test for AddTwoBinaryStrings
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestAddTwoBinaryStrings

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string1 = "111"
        input_string2 = "110"

        add_two_binaries_problem = AddTwoBinaryStrings(input_string1, input_string2)

        # Then
        self.assertEqual(add_two_binaries_problem.solve(), '1101')
