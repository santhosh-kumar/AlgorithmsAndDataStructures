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
                self.bridge_util(self.input_graph,
                                 vertex,
                                 visited_list,
                                 parents_list,
                                 discovery_times,
                                 low_values,
                                 traversal_counter,
                                 bridges)
        return bridges

    @staticmethod
    def bridge_util(input_graph, vertex, visited_list, parents_list, discovery_times, low, traversal_counter, bridges):
        """ Utility to find bridges

        Args:
            input_graph: input_graph
            vertex: vertex label
            visited_list: list of vertices to mark if they are visited or not
            parents_list: parents of the vertices
            discovery_times: Discovery time of the vertex
            low: Low values
            traversal_counter: Counter for graph traversal
            bridges: list of edges

        Returns:
            None

        Raises:
            None
        """
        # mark the current nodes as visited
        visited_list[vertex] = True

        # initialize the discovery time and low value
        discovery_times[vertex] = traversal_counter
        low[vertex] = traversal_counter

        traversal_counter = traversal_counter + 1

        # iterate through neighbors of the current vertex
        for neighbor_vertex in input_graph.graph[vertex]:
            # if the neighbor vertex is not visited
            if not visited_list[neighbor_vertex]:
                parents_list[neighbor_vertex] = vertex

                FindBridgesInAGraph.bridge_util(input_graph,
                                                neighbor_vertex,
                                                visited_list,
                                                parents_list,
                                                discovery_times,
                                                low,
                                                traversal_counter,
                                                bridges)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                low[vertex] = min(low[vertex], low[neighbor_vertex])

                ''' If the lowest vertex reachable from subtree 
                under neighbor_vertex is below vertex in DFS tree, then the edge is 
                a bridge'''
                if low[neighbor_vertex] > discovery_times[vertex]:
                    bridges.append((vertex, neighbor_vertex))

            elif neighbor_vertex != parents_list[vertex]:
                # Update low value of vertex for parent function calls
                low[vertex] = min(low[vertex], discovery_times[neighbor_vertex])
