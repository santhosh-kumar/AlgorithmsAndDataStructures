"""
Find Bridges in a Graph

An edge in an undirected connected graph is a bridge iff removing it disconnects the graph.
For a disconnected undirected graph, definition is similar, a bridge is an edge removing which increases number of disconnected components.

Like Articulation Points, bridges represent vulnerabilities in a connected network and are useful for designing reliable networks.

For example, in a wired computer network, an articulation point indicates the critical computers and a bridge indicates the critical wires or connections.
"""
from common.problem import Problem


class FindBridgesInAGraph(Problem):
    """
    FindBridgesInAGraph
    """
    PROBLEM_NAME = "FindBridgesInAGraph"

    def __init__(self, input_graph):
        """Find Bridges in a Graph (Undirected)

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

        Note: The idea is similar to O(V+E) algorithm for Articulation Points.
        We do DFS traversal of the given graph. In DFS tree an edge (u, v) (u is parent of v in DFS tree) is bridge
        if there does not exist any other alternative to reach u or an ancestor of u from subtree rooted with v.
        As discussed in the previous post, the value low[v] indicates earliest visited vertex reachable from subtree rooted with v.
        The condition for an edge (u, v) to be a bridge is, “low[v] > disc[u]”.

        Args:

        Returns:


        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        vertices = self.input_graph.get_vertices()

        # initialize the visited list and parents list
        visited_list = [False] * len(vertices)
        parents_list = [-1] * len(vertices)
        traversal_counter = 0

        discovery_times = [float('infinity')] * len(vertices)
        low_values = [float('infinity')] * len(vertices)

        bridges = []
        for vertex in vertices:
            if not visited_list[vertex]:
                self.input_graph.bridge_util(vertex,
                                             visited_list,
                                             parents_list,
                                             discovery_times,
                                             low_values,
                                             traversal_counter,
                                             bridges)
        return bridges
