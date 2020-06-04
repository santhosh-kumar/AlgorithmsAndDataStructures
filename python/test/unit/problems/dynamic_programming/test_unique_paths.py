"""
Unit Test for unique_paths
"""
from unittest import TestCase

from problems.dynamic_programming.unique_paths import UniquePaths


class TestUniquePaths(TestCase):
    """
    Unit test for UniquePaths
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestUniquePaths

        Returns:
            None

        Raises:
            None
        """
        # Given
        number_rows = 3
        number_columns = 7
        unique_paths_problem = UniquePaths(number_rows, number_columns)

        # When
        result = unique_paths_problem.solve()

        # Then
        self.assertEqual(result, 28)
