"""
Unit Test for find_connected_components
"""
from unittest import TestCase

from problems.graphs.find_connected_components import FindConnectedComponents


class TestFindConnectedComponents(TestCase):
    """
    Unit test for FindConnectedComponents
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestFindConnectedComponents

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
        adjacency_list = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5)]

        find_connected_components_problem = FindConnectedComponents(6, adjacency_list)

        # When
        result = find_connected_components_problem.solve()

        # Then
        self.assertEqual(result, 2)
