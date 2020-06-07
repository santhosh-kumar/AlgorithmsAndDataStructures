"""
Unit Test for topological_sorting_dag
"""
from unittest import TestCase

from common.graph import DirectedGraph
from problems.graphs.topological_sorting_dag import TopologicalSortingDAG


class TestTopologicalSortingDAG(TestCase):
    """
    Unit test for TopologicalSortingDAG
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestTopologicalSortingDAG

        Returns:
            None

        Raises:
            None
        """
        # Given
        '''
        Note : All the edges are Undirected 
        
        Given Graph: 
            5 ----> 0 <----- 4
            |                |
            |                |
            v                v
            2 ----> 3 -----> 1
        '''
        input_graph = DirectedGraph()
        input_graph.add_edge(5, 0)
        input_graph.add_edge(4, 0)
        input_graph.add_edge(5, 2)
        input_graph.add_edge(2, 3)
        input_graph.add_edge(3, 1)
        input_graph.add_edge(4, 1)

        topological_sort_problem = TopologicalSortingDAG(6, input_graph)

        # When
        result = topological_sort_problem.solve()

        # Then
        self.assertEqual(result, [5, 4, 2, 3, 1, 0])
