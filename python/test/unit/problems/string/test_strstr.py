"""
Unit Test for strstr
"""
from unittest import TestCase

from problems.string.strstr import StrStr


class TestStrStr(TestCase):
    """
    Unit test for StrStr
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestStrStr

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "mississippi"
        needle = "issi"
        strstr_problem = StrStr(input_string, needle)

        # When
        index = strstr_problem.solve()

        # Then
        self.assertEqual(index, 2)

    def test_solve_off_one(self):
        """Test solve (off one)

        Args:
            self: TestStrStr

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string = "aaaba"
        needle = "ba"
        strstr_problem = StrStr(input_string, needle)

        # When
        index = strstr_problem.solve()

        # Then
        self.assertEqual(index, 4)
