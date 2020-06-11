"""
Unit Test for all_pairs_shortest_path_floyd_warshall
"""
from unittest import TestCase

from problems.dynamic_programming.all_pairs_shortest_path_floyd_warshall import \
    AllPairsShortestPathsFloydWarshallAlgorithm


class TestAllPairsShortestPathsFloydWarshallAlgorithm(TestCase):
    """
    Unit test for AllPairsShortestPathsFloydWarshallAlgorithm
    """
    INF = float('infinity')

    def test_solve(self):
        """Test solve

        Args:
            self: TestAllPairsShortestPathsFloydWarshallAlgorithm

        Returns:
            None

        Raises:
            None
        """
        # Given

        """ 
            10 
       (0)------->(3) 
        |         /|\ 
      5 |          | 
        |          | 1 
       \|/         | 
       (1)------->(2) 
        """
        input_adjacency_matrix = [[0, 5, self.INF, 10], [self.INF, 0, 3, self.INF], [self.INF, self.INF, 0, 1],
                                  [self.INF, self.INF, self.INF, 0]]
        all_pair_shorted_problem = AllPairsShortestPathsFloydWarshallAlgorithm(input_adjacency_matrix)

        # When
        result = all_pair_shorted_problem.solve()

        # Then
        self.assertEqual(result, [[0, 5, 8, 9], [self.INF, 0, 3, 4], [self.INF, self.INF, 0, 1],
                                  [self.INF, self.INF, self.INF, 0]])
