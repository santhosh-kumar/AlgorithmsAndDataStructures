"""
Unit Test for unique_paths_with_obstacles
"""
from unittest import TestCase

from problems.dynamic_programming.unique_paths_with_obstacles import UniquePathsWithObstacles


class TestUniquePathsWithObstacles(TestCase):
    """
    Unit test for UniquePathsWithObstacles
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestUniquePathsWithObstacles

        Returns:
            None

        Raises:
            None
        """
        # Given
        obstacles_matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        unique_paths_problem = UniquePathsWithObstacles(obstacles_matrix)

        # When
        result = unique_paths_problem.solve()

        # Then
        self.assertEqual(result, 2)
