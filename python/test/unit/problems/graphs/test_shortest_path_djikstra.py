"""
Unit Test for shortest_path_djikstra
"""
from unittest import TestCase

from common.graph import UndirectedGraph
from problems.graphs.shortest_path_djikstra import ShortestPathDjikstrasAlgorithm


class TestShortestPathDjikstrasAlgorithm(TestCase):
    """
    Unit test for ShortestPathDjikstrasAlgorithm
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestShortestPathDjikstrasAlgorithm

        Returns:
            None

        Raises:
            None
        """
        # Given
        '''
        Note : All the edges are Undirected 
        Given Graph: 
        0--1 
        | | 
        3--2--4--5
        '''
        input_graph = UndirectedGraph()
        input_graph.add_edge(0, 1, 4) # u, v, weight
        input_graph.add_edge(1, 2, 3)
        input_graph.add_edge(2, 3, 1)
        input_graph.add_edge(3, 0, 2)
        input_graph.add_edge(2, 4, 3)
        input_graph.add_edge(4, 5, 2)

        shortest_path_problem = ShortestPathDjikstrasAlgorithm(input_graph)

        # When
        result = shortest_path_problem.solve()

        # Then
        self.assertEqual(result, {0: 0, 1: 4, 2: 3, 3: 2, 4: 6, 5: 8})
