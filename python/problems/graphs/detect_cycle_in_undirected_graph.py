"""
Given an undirected graph, how to check if there is a cycle in the graph?

For example,

1----2
| \  |
|  \ |
4----3

Has a cycle. 1->2->3->1

"""
from common.problem import Problem


class DetectCycleInUndirectedGraph(Problem):
    """
    Detect Cycle in a Undirected Graph
    """
    PROBLEM_NAME = "DetectCycleInUndirectedGraph"

    def __init__(self, input_graph):
        """Detect Cycle in Undirected Graph

        Args:
            input_graph: Graph

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_graph = input_graph

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

        vertices = self.input_graph.get_vertices()
        visited_dict = {}

        for vertex in vertices:
            visited_dict[vertex] = False

        for vertex in self.input_graph.get_vertices():
            if not visited_dict[vertex] and self.input_graph.is_cyclic(vertex, visited_dict, None):
                return True

        return False
