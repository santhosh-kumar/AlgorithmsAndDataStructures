"""
Unit Test for largest_rectangle_in_histogram
"""
from unittest import TestCase

from problems.stack.largest_rectangle_in_histogram import LargestRectangleInHistogram


class TestLargestRectangleInHistogram(TestCase):
    """
    Unit test for largest_rectangle_in_histogram
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestLargestRectangleInHistogram

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [6, 2, 5, 4, 5, 1, 6]
        largest_rectangle_problem = LargestRectangleInHistogram(input_list)

        # When
        result = largest_rectangle_problem.solve()

        # Then
        self.assertEqual(result, 12)
