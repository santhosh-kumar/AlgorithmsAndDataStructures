"""
Unit Test for missing_ranges
"""
from unittest import TestCase

from problems.array.missing_ranges import MissingRanges


class TestMissingRanges(TestCase):
    """
    Unit test for MissingRanges
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestMissingRanges

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [0, 1, 3, 50, 75]
        min_value = 0
        max_value = 99
        missing_ranges_problem = MissingRanges(input_list, min_value, max_value)

        # When
        range_list = missing_ranges_problem.solve()

        # Then
        self.assertEqual(range_list,  ["2", "4->49", "51->74", "76->99"])
