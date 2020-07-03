"""
This module defines graph related data structures and functions
"""
from abc import ABCMeta
from collections import defaultdict
from collections import deque

from common.stack import Stack


class GraphNode:
    """
    An element (vertex) in the graph
    """

    def __init__(self, data):
        """Init

        Args:
            data: Value of the node

        Returns:
            None

        Raises:
            None
        """
        super().__init__()
        self.data = data
        self.neighbors = []

    def add_neighbor(self, neighboring_node):
        """Add a neighbor to the graph

        Args:
            neighboring_node: Neighboring node

        Returns:
            None

        Raises:
            None
        """
        self.neighbors.append(neighboring_node)


class Graph:
    """
    Encapsulates Graph Related Operations (algorithms)
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        """Init

        Args:

        Returns:
            None

        Raises:
            None
        """
        self.graph = defaultdict(dict)

    def get_vertices_count(self):
        """Get the number of vertices

        Args:

        Returns:
            integer

        Raises:
            None
        """
        return len(self.get_vertices())

    def get_vertices(self):
        """Get list of vertices

        Args:

        Returns:
            list

        Raises:
            None
        """
        raise NotImplementedError

    def add_edge(self, u, v, weight=None):
        """Add an edge

        Args:
            u: first vertex
            v: second vertex
            weight: weight of the node (optional)

        Returns:
            None

        Raises:
            None
        """
        raise NotImplementedError

    def get_adjacency_list(self):
        """Returns the adjacency list (weight, u, v)

        Args:

        Returns:
            list(tuple)

        Raises:
            None
        """
        adjacency_list = []
        for u in self.get_vertices():
            for v in self.graph[u].keys():
                adjacency_list.append((self.graph[u][v], u, v))

        return adjacency_list

    def get_adjacency_list_for_vertex(self, u):
        """Returns the adjacency list (weight, u, v) for the vertex u

        Args:

        Returns:
            list(tuple)

        Raises:
            None
        """
        adjacency_list = []
        for v in self.graph[u].keys():
            adjacency_list.append((self.graph[u][v], u, v))

        return adjacency_list

    def get_neighbors(self, vertex):
        """Returns the neighbors of a particular node

        Args:

        Returns:
            list

        Raises:
            None
        """
        return list(self.graph[vertex].keys())

    @staticmethod
    def depth_first_traversal(graph_node, vertex_list):
        """Depth First Traversal of a Graph. Complexity is O(V+E).

        Args:
            graph_node: Starting node of the graph
            vertex_list: List of vertices traversed

        Returns:
            None

        Raises:
            None
        """
        nodes_stack = Stack()
        nodes_stack.push(graph_node)

        while len(nodes_stack) > 0:
            node = nodes_stack.pop()

            if node.data not in vertex_list:
                vertex_list.append(node.data)

                for neighbor_node in node.neighbors:
                    nodes_stack.push(neighbor_node)

    @staticmethod
    def breadth_first_traversal(graph_node, vertex_list):
        """Breadth First Traversal of a Graph. Complexity is O(V+E).

        Args:
            graph_node: Starting node of the graph
            vertex_list: List of vertices traversed (in|out)

        Returns:
            None

        Raises:
            None
        """
        nodes_queue = deque()
        nodes_queue.append(graph_node)

        while len(nodes_queue) > 0:
            node = nodes_queue.popleft()

            if node.data not in vertex_list:
                vertex_list.append(node.data)

                for neighbor_node in node.neighbors:
                    nodes_queue.append(neighbor_node)


class DirectedGraph(Graph):
    """
    Encapsulates DirectedGraph Graph
    """

    def add_edge(self, u, v, weight=None):
        """Add an edge

        Args:
            u: first vertex
            v: second vertex
            weight: weight of the node (optional)

        Returns:
            None

        Raises:
            None
        """
        self.graph[u][v] = weight

    def get_vertices(self):
        """Get list of vertices

        Args:

        Returns:
            list

        Raises:
            None
        """
        vertices = set()
        for vertex in self.graph.keys():
            vertices.add(vertex)
            for neighbor in self.graph[vertex].keys():
                vertices.add(neighbor)

        return list(vertices)


class UndirectedGraph(Graph):
    """
    Encapsulates Undirected Graph
    """

    def add_edge(self, u, v, weight=None):
        """Add an edge

        Args:
            u: first vertex
            v: second vertex
            weight: weight of the node (optional)
        """
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def get_vertices(self):
        """Get list of vertices

        Args:

        Returns:
            list

        Raises:
            None
        """
        return list(self.graph.keys())
