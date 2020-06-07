"""
Topological Sorting of DAG

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge
uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

For example, a topological sorting of the following graph is “5 4 2 3 1 0”.
There can be more than one topological sorting for a graph.

For example, another topological sorting of the following graph is “4 5 2 3 1 0”.
The first vertex in topological sorting is always a vertex with in-degree as 0 (a vertex with no incoming edges).

     5 ----> 0 <----- 4
     |                |
     |                |
     v                v
     2 ----> 3 -----> 1
"""
from common.problem import Problem


class TopologicalSortingDAG(Problem):
    """
    TopologicalSortingDAG
    """
    PROBLEM_NAME = "TopologicalSortingDAG"

    def __init__(self, number_vertices, input_graph):
        """Topological Sorting of DAG

        Args:
            number_vertices: Number of vertices in the graph
            input_graph: Graph for which to find the minimum spanning tree

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.number_vertices = number_vertices
        self.input_graph = input_graph

    def solve(self):
        """Solve the problem

        Note: O(V+E) solution is similar to the depth first search with a stack.

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        visited_list = [False] * self.number_vertices

        sort_list = []

        for vertex in range(self.number_vertices):
            if not visited_list[vertex]:
                self.input_graph.topological_sort_util(vertex, visited_list, sort_list)

        return sort_list
