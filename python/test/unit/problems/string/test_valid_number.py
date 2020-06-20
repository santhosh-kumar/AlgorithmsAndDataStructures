"""
Unit Test for valid_number
"""
from unittest import TestCase

from problems.string.valid_number import ValidNumber


class TestValidNumber(TestCase):
    """
    Unit test for ValidNumber
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestValidNumber

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "    +23972749"
        valid_number_problem = ValidNumber(input_string)

        # Then
        self.assertTrue(valid_number_problem.solve())

    def test_solve_with_space(self):
        """Test solve (number with space)

        Args:
            self: TestValidNumber

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "    +1 1"
        valid_number_problem = ValidNumber(input_string)

        # Then
        self.assertFalse(valid_number_problem.solve())

    def test_solve_decimal(self):
        """Test solve (decimal)

        Args:
            self: TestAtoI

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "    +23972.749"
        valid_number_problem = ValidNumber(input_string)

        # Then
        self.assertTrue(valid_number_problem.solve())
