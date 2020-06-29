"""
Hamiltonian Cycle in a Undirected Graph

Hamiltonian Path in an undirected graph is a path that visits each vertex exactly once.

A Hamiltonian cycle (or Hamiltonian circuit) is a Hamiltonian Path such that there is an edge (in the graph)
from the last vertex to the first vertex of the Hamiltonian Path.

Determine whether a given graph contains Hamiltonian Cycle or not. If it contains, then prints the path.
"""
from common.problem import Problem


class FindHamiltonianCycle(Problem):
    """
    FindHamiltonianCycle
    """
    PROBLEM_NAME = "FindHamiltonianCycle"

    def __init__(self, input_graph):
        """Find Hamiltonian in a Graph (Undirected)

        Args:
            input_graph: Graph for which to find the Hamiltonian Cycle

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_graph = input_graph

    def solve(self):
        """Solve the problem

        Note: It uses a backtracking based solution to add a vertex to the path only if it would lead to a hamiltonian cycle.

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        path = [0] * self.input_graph.get_vertices_count()

        if self.is_hamiltonian_cycle(path, 1):
            return path
        else:
            return []

    def is_hamiltonian_cycle(self, path, position):
        """Returns if the path is a Hamiltonian

        Args:
            path: Hamiltonian Path list
            position: Current position

        Returns:
            boolean

        Raises:
            None
        """
        # base case: if all vertices are included in the path
        if position == self.input_graph.get_vertices_count():
            last_vertex = path[position - 1]
            last_vertex_neighbors = self.input_graph.get_neighbors(last_vertex)

            # check if the first vertex is adjacent to the last vertex
            if path[0] in last_vertex_neighbors:
                return True
            else:
                return False

        # Check if the vertex could lead to hamiltonian cycle solution
        for vertex in range(1, self.input_graph.get_vertices_count()):
            if self.should_add_vertex(vertex, position, path):
                path[position] = vertex
                if self.is_hamiltonian_cycle(path, position + 1):
                    return True

                # Backtrack: Remove current vertex if it doesn't lead to a solution
                path[position] = -1

        return False

    def should_add_vertex(self, vertex, position, path):
        """Checks if the vertex is adjacent to the previously added vertex and not in the path

        Args:
            vertex: to check
            position: Current position
            path: Hamiltonian Path list

        Returns:
            boolean

        Raises:
            None
        """
        last_vertex = path[position - 1]
        last_vertex_neighbors = self.input_graph.get_neighbors(last_vertex)

        if vertex not in last_vertex_neighbors:
            return False

        if vertex in path:
            return False

        return True
