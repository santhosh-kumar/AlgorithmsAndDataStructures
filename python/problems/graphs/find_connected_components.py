"""
Find Connected Components

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to find the number of connected components in an undirected graph.

For example,

 0          3
 |          |
 1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
"""
from common.problem import Problem
from common.unionfind import UnionFind


class FindConnectedComponents(Problem):
    """
    FindConnectedComponents
    """
    PROBLEM_NAME = "FindConnectedComponents"

    def __init__(self, number_vertices, adjacency_list):
        """Find Connected Components

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
            Boolean

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        parent_list = [i for i in range(self.number_vertices)]

        union_find = UnionFind(parent_list)

        for i, j in self.adjacency_list:
            union_find.union(i, j)

        return len(set(parent_list))
