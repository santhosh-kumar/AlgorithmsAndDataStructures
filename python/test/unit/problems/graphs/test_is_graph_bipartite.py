"""
Unit Test for is_graph_bipartite
"""
from unittest import TestCase

from common.graph import GraphNode
from problems.graphs.is_graph_bipartite import IsGraphBipartite


class TestIsGraphBipartite(TestCase):
    """
    Unit test for IsGraphBipartite
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestIsGraphBipartite

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
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node3 = GraphNode(3)
        node4 = GraphNode(4)

        node1.add_neighbor(node2)
        node1.add_neighbor(node4)

        node2.add_neighbor(node3)
        node2.add_neighbor(node1)

        node3.add_neighbor(node4)
        node3.add_neighbor(node2)

        node4.add_neighbor(node1)
        node4.add_neighbor(node3)

        is_bipartite_problem = IsGraphBipartite(node1)

        # When
        result = is_bipartite_problem.solve()

        # Then
        self.assertTrue(result)

    def test_solve_invalid(self):
        """Test solve (invalid)

        Args:
            self: TestIsGraphBipartite

        Returns:
            None

        Raises:
            None
        """
        # Given
        '''
        Note : All the edges are Undirected 
        Given Graph: 
        1----2
        | \  |
        |  \ |
        4----3
        '''
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node3 = GraphNode(3)
        node4 = GraphNode(4)

        node1.add_neighbor(node2)
        node1.add_neighbor(node4)
        node1.add_neighbor(node3)

        node2.add_neighbor(node3)
        node2.add_neighbor(node1)

        node3.add_neighbor(node4)
        node3.add_neighbor(node2)
        node3.add_neighbor(node1)

        node4.add_neighbor(node1)
        node4.add_neighbor(node3)

        is_bipartite_problem = IsGraphBipartite(node1)

        # When
        result = is_bipartite_problem.solve()

        # Then
        self.assertFalse(result)
