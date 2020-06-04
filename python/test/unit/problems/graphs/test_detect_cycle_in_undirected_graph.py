"""
Unit Test for detect_cycle_in_undirected_graph
"""
from unittest import TestCase

from common.graph import UndirectedGraph
from problems.graphs.detect_cycle_in_undirected_graph import DetectCycleInUndirectedGraph


class TestDetectCycleInUndirectedGraph(TestCase):
    """
    Unit test for DetectCycleInUndirectedGraph
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestDetectCycleInUndirectedGraph

        Returns:
            None

        Raises:
            None
        """
        # Given
        '''
        Note : All the edges are Undirected 
        Given Graph: 
        1--2 
        | | 
        4--3 
        '''
        graph = UndirectedGraph()
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)
        graph.add_edge(4, 1)

        detect_cycle_problem = DetectCycleInUndirectedGraph(graph)

        # When
        result = detect_cycle_problem.solve()

        # Then
        self.assertTrue(result)

    def test_solve_not_a_cycle(self):
        """Test solve (not a cycle)

        Args:
            self: TestDetectCycleInUndirectedGraph

        Returns:
            None

        Raises:
            None
        """
        # Given
        '''
        Note : All the edges are Undirected 
        
        Given Graph: 
        1--2 
        |  | 
        4  3 
        '''
        graph = UndirectedGraph()
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(4, 1)

        detect_cycle_problem = DetectCycleInUndirectedGraph(graph)

        # When
        result = detect_cycle_problem.solve()

        # Then
        self.assertFalse(result)
