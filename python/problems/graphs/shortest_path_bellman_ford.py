"""
Compute Single Source Shortest Path (Bellman Ford's Algorithm)

Given a graph and a source vertex src in graph, find shortest paths from src to all vertices in the given graph.

The graph may contain negative weight edges. Dijkstra’s algorithm is a Greedy algorithm and time complexity is O(VLogV)
(with the use of Fibonacci heap). Dijkstra does not work for Graphs with negative weight edges, Bellman-Ford works for such graphs.

Bellman-Ford is also simpler than Dijkstra and suites well for distributed systems. But time complexity of Bellman-Ford is O(VE),
which is more than Dijkstra.
"""

from common.problem import Problem


class ShortestPathBellmanFordAlgorithm(Problem):
    """
    ShortestPathBellmanFordAlgorithm
    """
    PROBLEM_NAME = "ShortestPathBellmanFordAlgorithm"

    def __init__(self, input_graph, source):
        """Compute Shortest Path (Bellman Ford's Algorithm)

        Args:
            input_graph: Graph for which to find the shortest paths
            source: vertex
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_graph = input_graph
        self.source = source

    def solve(self):
        """Solve the problem

        Note: O(VE) (runtime) uses a relaxation technique by iterating the adjacency list V-1 times i.e.,
        distance[v] = distance[u] + w if distance[u]+w < distance[v].

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        # Step 1: Initialize distances from src to all other vertices as INFINITE
        distance = [float("Inf")] * self.input_graph.get_vertices_count()
        distance[self.source] = 0

        adjacency_list = self.input_graph.get_adjacency_list()

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.input_graph.get_vertices_count() - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for w, u, v in adjacency_list:
                if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.
        for w, u, v in adjacency_list:
            if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                return []

        return distance
