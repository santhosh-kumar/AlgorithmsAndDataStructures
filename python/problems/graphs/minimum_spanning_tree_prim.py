"""
Compute Minimum Spanning Tree (Prims's Algorithm)

Given a connected and undirected graph, a spanning tree of that graph is a sub-graph that is a tree and connects all the vertices together.
A single graph can have many different spanning trees.
A minimum spanning tree (MST) or minimum weight spanning tree for a weighted, connected and undirected graph is a spanning tree
with weight less than or equal to the weight of every other spanning tree.

The weight of a spanning tree is the sum of weights given to each edge of the spanning tree.

How many edges does a minimum spanning tree has?
A minimum spanning tree has (V – 1) edges where V is the number of vertices in the given graph.
"""
import heapq

from common.problem import Problem


class MinimumSpanningTreePrimsAlgorithm(Problem):
    """
    MinimumSpanningTreePrimsAlgorithm
    """
    PROBLEM_NAME = "MinimumSpanningTreePrimsAlgorithm"

    def __init__(self, input_graph):
        """Compute Minimum Spanning Tree (Prims's Algorithm)

        Args:
            input_graph: Graph for which to find the minimum spanning tree

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_graph = input_graph

    def solve(self):
        """Solve the problem

        Note: O(E logV) solution uses a heap to iterate every node and find the min weight edge.
        Then, for every minimum weight edge it does a heappush of its edges.

        Args:

        Returns:
            list(tuple)

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        minimum_spanning_tree_list = []

        # get the vertices
        vertices = self.input_graph.get_vertices()
        starting_vertex = vertices[0]

        # mark the starting vertex as visited
        visited = [starting_vertex]

        # get the edges from the starting vertex
        edges = self.input_graph.get_adjacency_list_for_vertex(starting_vertex)

        # heap priority is based on the weight, the first element in the tuple
        heapq.heapify(edges)

        # iterate through edges
        while edges:
            weight, u, v = heapq.heappop(edges)

            # if the neighbor is not visited, add it to the visited
            if v not in visited:
                visited.append(v)
                minimum_spanning_tree_list.append((weight, u, v))

                # find the edges from the to vertex
                to_edges = self.input_graph.get_adjacency_list_for_vertex(v)

                # add every edge from the to vertex to the heap
                for to_edge in to_edges:
                    weight1, u1, v1 = to_edge
                    if v1 not in visited:
                        heapq.heappush(edges, (weight1, v, v1))

        return minimum_spanning_tree_list
