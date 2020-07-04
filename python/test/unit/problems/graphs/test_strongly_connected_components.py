"""
Unit Test for strongly_connected_components
"""
from unittest import TestCase

from common.graph import DirectedGraph
from problems.graphs.strongly_connected_components import StronglyConnectedComponentKosarajuAlgorithm


class TestStronglyConnectedComponentKosarajuAlgorithm(TestCase):
    """
    Unit test for StronglyConnectedComponentKosarajuAlgorithm
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestStronglyConnectedComponentKosarajuAlgorithm

        Returns:
            None

        Raises:
            None
        """
        # Given
        '''
        Note : All the edges are Undirected 
        
        Given Graph:
         1 
        | | 
        2--0--3--4
        '''
        input_graph = DirectedGraph()
        input_graph.add_edge(1, 0)
        input_graph.add_edge(0, 2)
        input_graph.add_edge(2, 1)
        input_graph.add_edge(0, 3)
        input_graph.add_edge(3, 4)

        shortest_path_problem = StronglyConnectedComponentKosarajuAlgorithm(input_graph)

        # When
        result = shortest_path_problem.solve()

        # Then
        self.assertEqual(result, [[0, 1, 2], [3], [4]])
