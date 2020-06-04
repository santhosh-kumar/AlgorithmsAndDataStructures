"""
Unit Test for spiral_matrix
"""
from unittest import TestCase

from problems.misc.spiral_matrix import SpiralMatrix


class TestSpiralMatrix(TestCase):
    """
    Unit test for SpiralMatrix
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestSpiralMatrix

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        spiral_matrix_problem = SpiralMatrix(input_matrix)

        # When
        result = spiral_matrix_problem.solve()

        # Then
        self.assertEqual(result, [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])
