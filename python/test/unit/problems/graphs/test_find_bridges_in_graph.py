"""
Unit Test for find_bridges_in_graph
"""
from unittest import TestCase

from common.graph import UndirectedGraph
from problems.graphs.find_bridges_in_graph import FindBridgesInAGraph


class TestFindBridgesInAGraph(TestCase):
    """
    Unit test for FindBridgesInAGraph
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestFindBridgesInAGraph

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
        input_graph.add_edge(0, 1)
        input_graph.add_edge(1, 2)
        input_graph.add_edge(2, 3)
        input_graph.add_edge(3, 0)
        input_graph.add_edge(2, 4)
        input_graph.add_edge(4, 5)

        find_bridges_problem = FindBridgesInAGraph(input_graph)

        # When
        result = find_bridges_problem.solve()

        # Then
        self.assertEqual(result, [(4, 5), (2, 4)])
