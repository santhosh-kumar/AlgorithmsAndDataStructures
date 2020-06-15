"""
Max Flow (Ford Fulkerson)

Given a DIRECTED graph which represents a flow network where every edge has a capacity.
Also given two vertices source ‘s’ and sink ‘t’ in the graph, find the maximum possible flow from s to t with following constraints:

a) Flow on an edge doesnt exceed the given capacity of the edge.

b) Incoming flow is equal to outgoing flow for every vertex except s and t.
"""
from collections import deque

from common.problem import Problem


class MaxFlowFordFulkersonAlgorithm(Problem):
    """
    MaxFlowFordFulkersonAlgorithm
    """
    PROBLEM_NAME = "MaxFlowFordFulkersonAlgorithm"

    def __init__(self, input_capacity_matrix, source, sink):
        """Max Flow (Ford Fulkerson)

        Args:
            input_capacity_matrix: Graph with vertex to vertex capacities

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_capacity_matrix = input_capacity_matrix
        self.source = source
        self.sink = sink

    def solve(self):
        """Solve the problem

        Note: O(MAX_FLOW * E) solution works by using a residual graph.
            i. At each iteration, a check for a valid path between source and the sink is done using the BFS.

            ii. If there is a path, minimum path flow is calculated.

            iii. Update the capacity matrix by reducing the current minimum path flow and augmenting to the residual graph.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        max_rows = len(self.input_capacity_matrix)

        # Breadth first search will use this list to mark the parents for the path
        parent_list = [-1] * max_rows

        # initialize the max_flow to 0
        max_flow = 0

        # Augment the flow while there is path from source to sink
        while self.breadth_first_search(self.input_capacity_matrix, self.source, self.sink, parent_list):
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            min_path_flow = float("Inf")
            s = self.sink
            while s != self.source:
                min_path_flow = min(min_path_flow, self.input_capacity_matrix[parent_list[s]][s])
                s = parent_list[s]

            # Add path flow to overall flow
            max_flow += min_path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = self.sink

            while v != self.source:
                u = parent_list[v]
                self.input_capacity_matrix[u][v] -= min_path_flow
                self.input_capacity_matrix[v][u] += min_path_flow
                v = parent_list[v]

        return max_flow

    @staticmethod
    def breadth_first_search(capacity_matrix, source, sink, parents_list):
        """Breadth First Search

        Args:
            capacity_matrix: Input Capacity matrix
            source: vertex index
            sink: vertex index
            parents_list: parents for vertices

        Returns:
            boolean

        Raises:
            None
        """
        max_rows = len(capacity_matrix)

        # Mark all the vertices as not visited
        visited = [False] * max_rows

        # Deque for BFS
        vertex_queue = deque()

        # Mark the source node as visited and enqueue it
        vertex_queue.append(source)
        visited[source] = True

        while len(vertex_queue) > 0:
            # De-queue a vertex from queue and print it
            u = vertex_queue.popleft()

            # Get all adjacent vertices of the de-queued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(capacity_matrix[u]):
                print(capacity_matrix)
                print("{},{}".format(ind, val))
                if not visited[ind] and val > 0:
                    vertex_queue.append(ind)
                    visited[ind] = True
                    parents_list[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[sink] else False
