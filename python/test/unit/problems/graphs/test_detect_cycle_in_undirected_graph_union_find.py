"""
Unit Test for detect_cycle_in_undirected_graph (Union Find)
"""
from unittest import TestCase

from common.graph import UndirectedGraph
from problems.graphs.detect_cycle_in_undirected_graph_union_find import DetectCycleInUndirectedGraphUnionFind


class TestDetectCycleInUndirectedGraphUnionFind(TestCase):
    """
    Unit test for DetectCycleInUndirectedGraphUnionFind
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestDetectCycleInUndirectedGraphUnionFind

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
        3--2 
        '''
        graph = UndirectedGraph()
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 0)

        detect_cycle_problem = DetectCycleInUndirectedGraphUnionFind(graph)

        # When
        result = detect_cycle_problem.solve()

        # Then
        self.assertTrue(result)
