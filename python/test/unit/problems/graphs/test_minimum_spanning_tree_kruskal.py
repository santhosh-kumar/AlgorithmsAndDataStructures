"""
Unit Test for find_connected_components
"""
from unittest import TestCase

from problems.graphs.minimum_spanning_tree_kruskal import MinimumSpanningTreeKruskalsAlgorithm


class TestMinimumSpanningTreeKruskalsAlgorithm(TestCase):
    """
    Unit test for MinimumSpanningTreeKruskalsAlgorithm
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestMinimumSpanningTreeKruskalsAlgorithm

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
        3--2 4--5
        '''
        adjacency_list = [(0, 1, 4), (1, 2, 3), (2, 3, 1), (3, 0, 1), (2, 4, 3), (4, 5, 2)]

        min_spanning_tree_problem = MinimumSpanningTreeKruskalsAlgorithm(6, adjacency_list)

        # When
        result = min_spanning_tree_problem.solve()

        # Then
        self.assertEqual(result, [(2, 3, 1), (3, 0, 1), (4, 5, 2), (1, 2, 3), (2, 4, 3)])
