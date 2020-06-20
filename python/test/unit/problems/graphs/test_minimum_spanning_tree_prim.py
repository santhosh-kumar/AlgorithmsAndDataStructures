"""
Unit Test for minimum_spanning_tree_prim
"""
from unittest import TestCase

from common.graph import UndirectedGraph
from problems.graphs.minimum_spanning_tree_prim import MinimumSpanningTreePrimsAlgorithm


class TestMinimumSpanningTreePrimsAlgorithm(TestCase):
    """
    Unit test for MinimumSpanningTreePrimsAlgorithm
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestMinimumSpanningTreePrimsAlgorithm

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
        input_graph.add_edge(0, 1, 4)  # u, v, weight
        input_graph.add_edge(1, 2, 3)
        input_graph.add_edge(2, 3, 1)
        input_graph.add_edge(3, 0, 2)
        input_graph.add_edge(2, 4, 3)
        input_graph.add_edge(4, 5, 2)

        min_spanning_tree_problem = MinimumSpanningTreePrimsAlgorithm(input_graph)

        # When
        result = min_spanning_tree_problem.solve()

        # Then
        self.assertEqual(result, [(2, 0, 3), (1, 3, 2), (3, 2, 1), (3, 2, 4), (2, 4, 5)])
