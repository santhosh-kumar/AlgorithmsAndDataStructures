"""
Strongly Connected Components (Kosaraju's Algorithm)

A directed graph is strongly connected if there is a path between all pairs of vertices.
A strongly connected component (SCC) of a directed graph is a maximal strongly connected sub-graph.
"""

from common.problem import Problem
from common.stack import Stack


class StronglyConnectedComponentKosarajuAlgorithm(Problem):
    """
    StronglyConnectedComponentKosarajuAlgorithm
    """
    PROBLEM_NAME = "StronglyConnectedComponentKosarajuAlgorithm"

    def __init__(self, input_graph):
        """Compute Shortest Path (Bellman Ford's Algorithm)

        Args:
            input_graph: Graph for which to find the shortest paths

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_graph = input_graph

    def solve(self):
        """Solve the problem

        Note: We can find all strongly connected components in O(V+E) time using Kosaraju’s algorithm.

        Following is detailed Kosaraju’s algorithm.

        1)  Create an empty stack ‘S’ and do DFS traversal of a graph.
            In DFS traversal, after calling recursive DFS for adjacent vertices of a vertex, push the vertex to stack.
            In the above graph, if we start DFS from vertex 0, we get vertices in stack as 1, 2, 4, 3, 0.

        2) Reverse directions of all arcs to obtain the transpose graph.

        3) One by one pop a vertex from S while S is not empty. Let the popped vertex be ‘v’. Take v as source and do DFS (call DFSUtil(v)).
        The DFS starting from v prints strongly connected component of v.

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        vertices_count = self.input_graph.get_vertices_count()
        stack = Stack()

        visited = [False] * vertices_count

        # Fill vertices in stack according to their finishing times
        for v in range(vertices_count):
            if not visited[v]:
                self.fill_order(v, visited, stack)

        reversed_graph = self.input_graph.reverse()

        # Mark all the vertices as not visited (For second DFS)
        visited = [False] * vertices_count

        # Now process all vertices in order defined by Stack
        strongly_connected_components = []
        while stack:
            vertex = stack.pop()
            vertex_list = []
            if not visited[vertex]:
                reversed_graph.dfs_util(vertex, visited, vertex_list)

            if len(vertex_list) > 0:
                strongly_connected_components.append(vertex_list)

        return strongly_connected_components

    def fill_order(self, vertex, visited, stack):
        """Compute Shortest Path (Bellman Ford's Algorithm)

        Args:
            vertex: node
            visited: list of visited nodes
            stack: node stack

        Returns:
            None

        Raises:
            None
        """
        # Mark the current node as visited
        visited[vertex] = True

        # Recur for all the vertices adjacent to this vertex
        for neighbor_vertex in self.input_graph.graph[vertex].keys():
            if not visited[neighbor_vertex]:
                self.fill_order(neighbor_vertex, visited, stack)
        stack.push(vertex)
