"""
Unit Test for rotate_matrix
"""
from unittest import TestCase

from problems.misc.rotate_matrix import RotateMatrix


class TestRotateMatrix(TestCase):
    """
    Unit test for RotateMatrix
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestRotateMatrix

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        rotate_matrix_problem = RotateMatrix(input_matrix)

        # When
        result = rotate_matrix_problem.solve()

        # Then
        self.assertEqual(result, [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]])
