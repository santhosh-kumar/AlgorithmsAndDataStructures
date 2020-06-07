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
        return len(self.graph.keys())

    def get_vertices(self):
        """Get list of vertices

        Args:

        Returns:
            list

        Raises:
            None
        """
        return list(self.graph.keys())

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

    @staticmethod
    def depth_first_traversal(graph_node, vertex_list):
        """Depth First Traversal of a Graph

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
        """Breadth First Traversal of a Graph

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

    def is_cyclic(self, vertex, visited_dict, parent):
        """ Check if the given node is part of a cycle

        Args:
            vertex: label of the vertex to be checked
            visited_dict: dict of vertices to mark if they are visited or not
            parent: label for the parent vertex

        Returns:
            None

        Raises:
            None
        """
        # Mark the current node as visited
        visited_dict[vertex] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[vertex]:
            # If the node is not visited then recurse on it
            if not visited_dict[i]:
                if self.is_cyclic(i, visited_dict, vertex):
                    return True

            # If an adjacent vertex is visited and not parent of current vertex,
            # then there is a cycle
            elif parent != i:
                return True

        return False
