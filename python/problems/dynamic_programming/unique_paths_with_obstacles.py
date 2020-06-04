"""
Unique Paths (with obstacles)

A robot is located at the top-left corner of a m × n grid (marked ‘Start’ in the diagram
below).

The robot can only move either down or right at any point in time. The robot is
trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram
below).

But now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space are marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3×3 grid as illustrated below.
[
 [0,0,0],
 [0,1,0],
 [0,0,0]
]
The total number of unique paths is 2.
"""
from common.problem import Problem


class UniquePathsWithObstacles(Problem):
    """
    Unique Paths (with obstacles)
    """
    PROBLEM_NAME = "UniquePathsWithObstacles"

    def __init__(self, obstacles_matrix):
        """Unique Paths

        Args:
            obstacles_matrix: contains the locations of the obstacles
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.obstacles_matrix = obstacles_matrix

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

        m = len(self.obstacles_matrix[:])
        n = len(self.obstacles_matrix[0])

        path_matrix = [[-1 for i in range(n)] for j in range(m)]
        path_matrix[m - 2][n - 1] = 1

        for i in range(m):
            path_matrix[i][n - 1] = 1

        for i in range(n):
            path_matrix[m - 1][i] = 1

        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                if self.obstacles_matrix[r][c] != 1:
                    path_matrix[r][c] = path_matrix[r + 1][c] + path_matrix[r][c + 1]
                else:
                    path_matrix[r][c] = 0

        return path_matrix[0][0]
