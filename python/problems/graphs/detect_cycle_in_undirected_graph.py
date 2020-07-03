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
            if not visited_dict[vertex] and self.is_cyclic(self.input_graph, vertex, visited_dict, None):
                return True

        return False

    @staticmethod
    def is_cyclic(input_graph, vertex, visited_dict, parent):
        """ Check if the given node is part of a cycle

        Args:
            input_graph: input graph
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
        for neighbor_vertex in input_graph.graph[vertex]:
            # If the node is not visited then recurse on it
            if not visited_dict[neighbor_vertex]:
                if DetectCycleInUndirectedGraph.is_cyclic(input_graph, neighbor_vertex, visited_dict, vertex):
                    return True

            # If an adjacent vertex is visited and not parent of current vertex,
            # then there is a cycle
            elif parent != neighbor_vertex:
                return True

        return False
