"""
Unit Test for all_pairs_shortest_path_floyd_warshall
"""
from unittest import TestCase

from problems.graphs.max_flow_ford_fulkerson import MaxFlowFordFulkersonAlgorithm


class TestMaxFlowFordFulkersonAlgorithm(TestCase):
    """
    Unit test for MaxFlowFordFulkersonAlgorithm
    """
    INF = float('infinity')

    def test_solve(self):
        """Test solve

        Args:
            self: TestMaxFlowFordFulkersonAlgorithm

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
        max_flow_problem = MaxFlowFordFulkersonAlgorithm(input_capacity_matrix, 0, 5)

        # When
        result = max_flow_problem.solve()

        # Then
        self.assertEqual(result, 23)
