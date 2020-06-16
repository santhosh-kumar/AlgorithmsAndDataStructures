"""
Unit Test for all_pairs_shortest_path_floyd_warshall
"""
from unittest import TestCase

from problems.graphs.min_cut import MinCut


class TestMinCut(TestCase):
    """
    Unit test for MinCut
    """
    INF = float('infinity')

    def test_solve(self):
        """Test solve

        Args:
            self: TestMinCut

        Returns:
            None

        Raises:
            None
        """
        # Given

        input_capacity_matrix = [[0, 16, 13, 0, 0, 0],
                                 [0, 0, 10, 12, 0, 0],
                                 [0, 4, 0, 0, 14, 0],
                                 [0, 0, 9, 0, 0, 20],
                                 [0, 0, 0, 7, 0, 4],
                                 [0, 0, 0, 0, 0, 0]]
        min_cut_problem = MinCut(input_capacity_matrix, 0, 5)

        # When
        result = min_cut_problem.solve()

        # Then
        self.assertEqual(result, [(1, 3), (4, 3), (4, 5)])
