"""
Unit Test for intersection_of_sorted_arrays
"""
from unittest import TestCase

from problems.array.intersection_of_sorted_arrays import IntersectionOfSortedArrays


class TestIntersectionOfSortedArrays(TestCase):
    """
    Unit test for IntersectionOfSortedArrays
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestIntersectionOfSortedArrays

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list1 = [2, 5, 6, 7, 8, 9]
        input_list2 = [3, 7, 9, 11, 14]
        intersection_problem = IntersectionOfSortedArrays(input_list1, input_list2)

        # When
        result = intersection_problem.solve()

        # Then
        self.assertEqual(result, [7, 9])
