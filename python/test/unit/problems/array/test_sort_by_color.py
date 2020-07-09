"""
Unit Test for sort_by_color
"""
from unittest import TestCase

from problems.array.sort_by_color import SortByColor


class TestSortByColor(TestCase):
    """
    Unit test for SortByColor
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestSortByColor

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
        sort_by_color = SortByColor(input_list)

        # When
        result = sort_by_color.solve()

        # Then
        self.assertEqual(result, [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2])
