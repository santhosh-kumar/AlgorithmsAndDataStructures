"""
Min Cut

Given a DIRECTED graph which represents a flow network where every edge has a capacity.
Also given two vertices source ‘s’ and sink ‘t’ in the graph.

In a flow network, an s-t cut is a cut that requires the source ‘s’ and the sink ‘t’ to be in different subsets,
and it consists of edges going from the source’s side to the sink’s side.

The capacity of an s-t cut is defined by the sum of the capacity of each edge in the cut-set.
"""
from collections import deque

from common.problem import Problem
from copy import deepcopy


class MinCut(Problem):
    """
    MinCut
    """
    PROBLEM_NAME = "MinCut"

    def __init__(self, input_capacity_matrix, source, sink):
        """Min Cut

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

            The max-flow min-cut theorem states that in a flow network, the amount of maximum flow is equal to capacity of the minimum cut.

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        original_capacity_matrix = deepcopy(self.input_capacity_matrix)

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
                self.input_capacity_matrix[u][v] = self.input_capacity_matrix[u][v] - min_path_flow
                self.input_capacity_matrix[v][u] = self.input_capacity_matrix[v][u] - min_path_flow
                v = parent_list[v]

        # print the edges which initially had weights
        # but now have 0 weight
        min_cut_edges = []
        for i in range(len(self.input_capacity_matrix)):
            for j in range(len(self.input_capacity_matrix[0])):
                if self.input_capacity_matrix[i][j] == 0 and original_capacity_matrix[i][j] > 0:
                    min_cut_edges.append((i, j))

        return min_cut_edges

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
                if not visited[ind] and val > 0:
                    vertex_queue.append(ind)
                    visited[ind] = True
                    parents_list[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[sink] else False
