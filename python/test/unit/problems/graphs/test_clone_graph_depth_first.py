"""
Unit Test for clone_graph_depth_first
"""
from unittest import TestCase

from common.graph import Graph
from common.graph import GraphNode
from problems.graphs.clone_graph_depth_first import CloneGraphDepthFirst


class TestCloneGraphDepthFirst(TestCase):
    """
    Unit test for CloneGraphDepthFirst
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestCloneGraphDepthFirst

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

        clone_graph_problem = CloneGraphDepthFirst(node1)

        # When
        cloned_graph_node = clone_graph_problem.solve()

        # Then
        cloned_list = []
        Graph.depth_first_traversal(cloned_graph_node, cloned_list)

        input_list = []
        Graph.depth_first_traversal(node1, input_list)

        self.assertEqual(cloned_list, input_list)
