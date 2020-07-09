"""
Rotate Matrix (by 90 Degrees Anti-clockwise)

Given a square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra space.

Examples:

Input:
 1  2  3
 4  5  6
 7  8  9

Output:
 3  6  9
 2  5  8
 1  4  7
"""
from math import floor

from common.problem import Problem


class RotateMatrix(Problem):
    """
    Rotate Matrix
    """
    PROBLEM_NAME = "RotateMatrix"

    def __init__(self, input_matrix):
        """Rotate Matrix

        Args:
            input_matrix: Input matrix

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_matrix = input_matrix

    def solve(self):
        """Solve the problem

        Note:  O(n^2) runtime and O(1) (space)

        Args:

        Returns:
            2-D array

        Raises:
            None
        """
        if len(self.input_matrix) == 0:
            return None

        m = len(self.input_matrix)
        n = len(self.input_matrix[0])

        if m != n:
            return None

        x = int(floor(n / 2))
        y = n - 1

        for i in range(x):
            for j in range(i, y - i, 1):
                # store current cell in temp variable
                temp = self.input_matrix[i][j]

                # move values from right to top
                self.input_matrix[i][j] = self.input_matrix[y - j][i]

                # move values from bottom to right
                self.input_matrix[y - j][i] = self.input_matrix[y - i][y - j]

                # move values from left to bottom
                self.input_matrix[y - i][y - j] = self.input_matrix[j][y - i]

                # assign temp to left
                self.input_matrix[j][y - i] = temp

        return self.input_matrix
