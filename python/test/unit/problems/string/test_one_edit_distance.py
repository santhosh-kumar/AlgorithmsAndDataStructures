"""
Unit Test for one_edit_distance
"""
from unittest import TestCase

from problems.string.one_edit_distance import OneEditDistance


class TestOneEditDistance(TestCase):
    """
    Unit test for OneEditDistance
    """

    def test_solve_modify(self):
        """Test solve (modify operation)

        Args:
            self: TestOneEditDistance

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string1 = "abcde"
        input_string2 = "abXde"
        one_edit_distance_problem = OneEditDistance(input_string1, input_string2)

        # When
        result = one_edit_distance_problem.solve()

        # Then
        self.assertTrue(result)

    def test_solve_append(self):
        """Test solve (append operation)

        Args:
            self: TestOneEditDistance

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string1 = "abcde"
        input_string2 = "abcdeX"
        one_edit_distance_problem = OneEditDistance(input_string1, input_string2)

        # When
        result = one_edit_distance_problem.solve()

        # Then
        self.assertTrue(result)

    def test_solve_insertion(self):
        """Test solve (insertion operation)

        Args:
            self: TestOneEditDistance

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string1 = "abcde"
        input_string2 = "abcXde"
        one_edit_distance_problem = OneEditDistance(input_string1, input_string2)

        # When
        result = one_edit_distance_problem.solve()

        # Then
        self.assertTrue(result)
