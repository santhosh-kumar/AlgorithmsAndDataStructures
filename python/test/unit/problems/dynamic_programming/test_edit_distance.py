"""
Unit Test for EditDistance
"""
from unittest import TestCase

from problems.dynamic_programming.edit_distance import EditDistance


class TestEditDistance(TestCase):
    """
    Unit test for EditDistance
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestEditDistance

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_string1 = "sunday"
        input_string2 = "saturday"
        edit_distance_problem = EditDistance(input_string1, input_string2)

        # When
        result = edit_distance_problem.solve()

        # Then
        self.assertEqual(result, 3)
