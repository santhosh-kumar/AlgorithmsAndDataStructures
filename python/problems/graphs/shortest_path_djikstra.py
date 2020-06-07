"""
Compute Shortest Path (Djikstra's Algorithm)

Given a graph and a source vertex in the graph, find shortest paths from source to all vertices in the given graph.
Dijkstra’s algorithm is very similar to Prim’s algorithm for minimum spanning tree.
"""
from common.problem import Problem
import heapq


class ShortestPathDjikstrasAlgorithm(Problem):
    """
    ShortestPathDjikstrasAlgorithm
    """
    PROBLEM_NAME = "ShortestPathDjikstrasAlgorithm"

    def __init__(self, input_graph):
        """Compute Shortest Path (Djikstra's Algorithm)

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

        Note: O(E log V) solution works using a heap for the adjacent nodes and performing a greeding approach for choosing
        the next node.

        Args:

        Returns:
            dict

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        vertices = self.input_graph.get_vertices()
        starting_vertex = vertices[0]

        # initialize distances to all the other other vertex from the starting vertex as infinity
        distances = {vertex: float('infinity') for vertex in vertices}
        distances[starting_vertex] = 0

        # construct a priority queue with the starting_vertex
        priority_queue = [(0, starting_vertex)]
        heapq.heapify(priority_queue)

        # if there are items in the priority queue
        while len(priority_queue) > 0:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # discard nodes that are farther than the current
            if current_distance > distances[current_vertex]:
                continue

            # get the neighbors of the current vertex
            adjacency_list = self.input_graph.get_adjacency_list_for_vertex(current_vertex)

            # iterate through the neighbors and calculate distances
            for i in range(len(adjacency_list)):
                weight, _, neighbor_vertex = adjacency_list[i]

                # calculate the distance to the neighboring vertex
                distance = weight + current_distance

                # if it's closer than the current distance, update the distance and add it to the heap
                if distance < distances[neighbor_vertex]:
                    distances[neighbor_vertex] = distance
                    heapq.heappush(priority_queue, (distance, neighbor_vertex))

        return distances
