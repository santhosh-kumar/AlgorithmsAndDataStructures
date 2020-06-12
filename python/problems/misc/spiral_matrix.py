"""
Spiral Matrix

Given a matrix of m ✕ n elements (m rows, n columns), return all elements of the
matrix in spiral order.
For example, given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""
from common.problem import Problem


class SpiralMatrix(Problem):
    """
    Spiral Matrix
    """
    PROBLEM_NAME = "SpiralMatrix"

    def __init__(self, input_matrix):
        """Spiral Matrix

        Args:
            input_matrix: Input matrix

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_matrix = input_matrix
        self.spiral_list = []

    def solve(self):
        """Solve the problem

        Note: O(mn) (runtime) and O(1) (space) works by iterating rows and columns while decreasing the max_row and max_columns becomes 0.

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        self.print_spiral_matrix(len(self.input_matrix), len(self.input_matrix[0]))
        return self.spiral_list

    def print_spiral_matrix(self, max_row, max_column):
        """Print Spiral Matrix

        Args:
            max_row: Max rows to consider
            max_column: Max columns to consider

        Returns:
            None

        Raises:
            None
        """
        if max_row == 0 or max_column == 0:
            return

        row_index = 0
        column_index = -1

        while True:
            for i in range(max_column):
                column_index = column_index + 1
                self.spiral_list.append(self.input_matrix[row_index][column_index])

            max_row = max_row - 1
            if max_row == 0:
                break

            for i in range(max_row):
                row_index = row_index + 1
                self.spiral_list.append(self.input_matrix[row_index][column_index])

            max_column = max_column - 1
            if max_column == 0:
                break

            for i in range(max_column):
                column_index = column_index - 1
                self.spiral_list.append(self.input_matrix[row_index][column_index])

            max_row = max_row - 1
            if max_row == 0:
                break

            for i in range(max_row):
                row_index = row_index - 1
                self.spiral_list.append(self.input_matrix[row_index][column_index])

            max_column = max_column - 1
            if max_column == 0:
                break
