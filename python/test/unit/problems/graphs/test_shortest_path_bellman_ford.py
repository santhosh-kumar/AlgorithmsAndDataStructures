"""
Unit Test for shortest_path_bellman_ford
"""
from unittest import TestCase

from common.graph import DirectedGraph
from problems.graphs.shortest_path_bellman_ford import ShortestPathBellmanFordAlgorithm


class TestShortestPathBellmanFordAlgorithm(TestCase):
    """
    Unit test for ShortestPathBellmanFordAlgorithm
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestShortestPathBellmanFordAlgorithm

        Returns:
            None

        Raises:
            None
        """
        # Given
        '''
        Note : All the edges are Undirected 
        '''
        input_graph = DirectedGraph()
        input_graph.add_edge(0, 1, -1)
        input_graph.add_edge(0, 2, 4)
        input_graph.add_edge(1, 2, 3)
        input_graph.add_edge(1, 3, 2)
        input_graph.add_edge(1, 4, 2)
        input_graph.add_edge(3, 2, 5)
        input_graph.add_edge(3, 1, 1)
        input_graph.add_edge(4, 3, -3)

        source = 0

        shortest_path_problem = ShortestPathBellmanFordAlgorithm(input_graph, source)

        # When
        result = shortest_path_problem.solve()

        # Then
        self.assertEqual(result, [0, -1, 2, -2, 1])
