"""
Unit Test for binary_tree
"""
from unittest import TestCase

from common.graph import DirectedGraph
from common.graph import Graph
from common.graph import GraphNode
from common.graph import UndirectedGraph


class TestGraph(TestCase):
    """
    Unit test for Graph
    """

    def test_depth_first_traversal(self):
        """Test for graph node (depth_first_traversal)

        Args:
            self: TestGraph

        Returns:
            None

        Raises:
            None
        """
        # Given
        '''
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

        # When
        result = []
        Graph.depth_first_traversal(node1, result)

        # Then
        self.assertEqual(result, [1, 4, 3, 2])

    def test_breadth_first_traversal(self):
        """Test for graph node (breadth_first_traversal)

        Args:
            self: TestGraph

        Returns:
            None

        Raises:
            None
        """
        # Given
        '''
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

        # When
        result = []
        Graph.breadth_first_traversal(node1, result)

        # Then
        self.assertEqual(result, [1, 2, 4, 3])

    def test_directed_graph(self):
        """Test for DirectedGraph

        Args:
            self: TestGraph

        Returns:
            None

        Raises:
            None
        """
        # Given
        '''
        Note : All the edges are Directed 
        
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

        # Then
        self.assertEqual(input_graph.get_vertices(), [0, 1, 2, 3, 4, 5])
        self.assertEqual(input_graph.get_vertices_count(), 6)
        self.assertEqual(input_graph.get_neighbors(5), [0, 2])
        self.assertEqual(input_graph.get_neighbors(0), [])
        self.assertEqual(input_graph.get_neighbors(2), [3])
        self.assertEqual(input_graph.get_neighbors(3), [1])
        self.assertEqual(input_graph.get_neighbors(4), [0, 1])
        self.assertEqual(input_graph.get_neighbors(1), [])
        self.assertEqual(input_graph.get_adjacency_list(), [(None, 2, 3),
                                                            (None, 3, 1),
                                                            (None, 4, 0),
                                                            (None, 4, 1),
                                                            (None, 5, 0),
                                                            (None, 5, 2)])
        self.assertEqual(input_graph.get_adjacency_list_for_vertex(5), [(None, 5, 0),
                                                                        (None, 5, 2)])

    def test_undirected_graph(self):
        """Test for UnDirectedGraph

        Args:
            self: TestGraph

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

        # Then
        self.assertEqual(graph.get_vertices(), [1, 2, 3, 4])
        self.assertEqual(graph.get_vertices_count(), 4)
        self.assertEqual(graph.get_neighbors(1), [2, 4])
        self.assertEqual(graph.get_neighbors(2), [1, 3])
        self.assertEqual(graph.get_neighbors(3), [2, 4])
        self.assertEqual(graph.get_neighbors(4), [3, 1])
        self.assertEqual(graph.get_adjacency_list(), [(None, 1, 2),
                                                      (None, 1, 4),
                                                      (None, 2, 1),
                                                      (None, 2, 3),
                                                      (None, 3, 2),
                                                      (None, 3, 4),
                                                      (None, 4, 3),
                                                      (None, 4, 1)])
        self.assertEqual(graph.get_adjacency_list_for_vertex(1), [(None, 1, 2), (None, 1, 4)])
