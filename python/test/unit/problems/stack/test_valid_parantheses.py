"""
Unit Test for valid_parantheses
"""
from unittest import TestCase

from problems.stack.valid_parantheses import ValidParantheses


class TestValidParantheses(TestCase):
    """
    Unit test for ValidParantheses
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestValidParantheses

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "()[]{}"
        valid_parantheses_problem = ValidParantheses(input_string)

        # Then
        self.assertTrue(valid_parantheses_problem.solve())

    def test_solve_in_valid(self):
        """Test solve (in valid)

        Args:
            self: TestValidParantheses

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "([)]"
        valid_parantheses_problem = ValidParantheses(input_string)

        # Then
        self.assertFalse(valid_parantheses_problem.solve())
