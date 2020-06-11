"""
All Pairs Shortest Path (Floyd Warshall Algorithm)

The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem.

The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph.
"""
from common.problem import Problem


class AllPairsShortestPathsFloydWarshallAlgorithm(Problem):
    """
    AllPairsShortestPathsFloydWarshallAlgorithm
    """
    PROBLEM_NAME = "AllPairsShortestPathsFloydWarshallAlgorithm"

    def __init__(self, input_adjacency_matrix):
        """All Pairs Shortest Path (Floyd Warshall)

        Args:
            input_adjacency_matrix: Graph for which to find the minimum spanning tree

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_adjacency_matrix = input_adjacency_matrix

    def solve(self):
        """Solve the problem

        Note: O(n^3) (runtime) and O(1) (space) solution works by considering a single node (k) and calculating the minimum of
        weights between a[i][j] and a[i][k] + a[k][j]

        Args:

        Returns:
            dict

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        number_nodes = len(self.input_adjacency_matrix[0])

        for k in range(number_nodes):
            for i in range(number_nodes):
                for j in range(number_nodes):
                    self.input_adjacency_matrix[i][j] = min(self.input_adjacency_matrix[i][j],
                                                            self.input_adjacency_matrix[i][k] +
                                                            self.input_adjacency_matrix[k][j])

        return self.input_adjacency_matrix



