"""
Unit Test for four_equal
"""
from unittest import TestCase

from problems.hashing.four_equal import FourEqual


class TestFourEqual(TestCase):
    """
    Unit test for FourEqual
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestFourEqual

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [3, 4, 7, 1, 2, 9, 8]
        four_equal_problem = FourEqual(input_list)

        # When
        result = four_equal_problem.solve()

        # Then
        expected_result = [[3, 8, 4, 7],
                           [3, 2, 4, 1],
                           [3, 9, 4, 8],
                           [3, 7, 1, 9],
                           [7, 2, 1, 8],
                           [3, 8, 2, 9],
                           [3, 7, 2, 8]]

        self.assertEqual(result, expected_result)
