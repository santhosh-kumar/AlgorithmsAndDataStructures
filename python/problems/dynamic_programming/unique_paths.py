"""
Unique Paths

A robot is located at the top-left corner of a m × n grid (marked ‘Start’ in the diagram
below).

The robot can only move either down or right at any point in time. The robot is
trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram
below).

How many possible unique paths are there?
"""
from common.problem import Problem


class UniquePaths(Problem):
    """
    Unique Paths
    """
    PROBLEM_NAME = "UniquePaths"

    def __init__(self, number_rows, number_columns):
        """Unique Paths

        Args:
            number_rows: Number of rows in the matrix
            number_columns: Number of columns in the matrix
        Returns:
            None

        Raises:
            None
        """
        assert (number_rows > 0)
        assert (number_columns > 0)

        super().__init__(self.PROBLEM_NAME)
        self.number_rows = number_rows
        self.number_columns = number_columns

    def solve(self):
        """Solve the problem

        Note: O(mn) solution works by using the dynamic programming to calculate total unique paths using the
        the sum of total unique paths from grid to the right (r, c + 1) and the grid below (r + 1, c).

        Args:

        Returns:
            tuple

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        m = self.number_rows
        n = self.number_columns

        path_matrix = [[-1 for i in range(n)] for j in range(m)]
        path_matrix[m - 2][n - 1] = 1

        for i in range(m):
            path_matrix[i][n - 1] = 1

        for i in range(n):
            path_matrix[m - 1][i] = 1

        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                path_matrix[r][c] = path_matrix[r + 1][c] + path_matrix[r][c + 1]

        return path_matrix[0][0]
