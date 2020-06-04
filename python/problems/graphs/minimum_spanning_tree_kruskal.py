"""
Compute Minimum Spanning Tree (Kruskal's Algorithm)

Given a connected and undirected graph, a spanning tree of that graph is a sub-graph that is a tree and connects all the vertices together.
A single graph can have many different spanning trees.
A minimum spanning tree (MST) or minimum weight spanning tree for a weighted, connected and undirected graph is a spanning tree
with weight less than or equal to the weight of every other spanning tree.

The weight of a spanning tree is the sum of weights given to each edge of the spanning tree.

How many edges does a minimum spanning tree has?
A minimum spanning tree has (V – 1) edges where V is the number of vertices in the given graph.
"""
from common.problem import Problem
from common.unionfind import UnionFind


class MinimumSpanningTreeKruskalsAlgorithm(Problem):
    """
    MinimumSpanningTreeKruskalsAlgorithm
    """
    PROBLEM_NAME = "MinimumSpanningTreeKruskalsAlgorithm"

    def __init__(self, number_vertices, adjacency_list):
        """Compute Minimum Spanning Tree (Kruskal's Algorithm)

        Args:
            number_vertices: Number of vertices
            adjacency_list: Adjacency List

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.number_vertices = number_vertices
        self.adjacency_list = adjacency_list

    def solve(self):
        """Solve the problem

        Note:

        Args:

        Returns:
            list(list)

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        result = []

        sorted_edges_index = 0
        edge_index = 0

        # sort the items based on the weight
        self.adjacency_list = sorted(self.adjacency_list, key=lambda item: item[2])

        parents = [i for i in range(self.number_vertices)]
        union_find = UnionFind(parents)

        while edge_index < self.number_vertices - 1:
            vertex1, vertex2, weight = self.adjacency_list[sorted_edges_index]

            vertex1_parent_index = union_find.find(vertex1)
            vertex2_parent_index = union_find.find(vertex2)

            if vertex1_parent_index != vertex2_parent_index:
                edge_index = edge_index + 1
                result.append(self.adjacency_list[sorted_edges_index])
                union_find.union(vertex1, vertex2)

            sorted_edges_index = sorted_edges_index + 1

        return result
