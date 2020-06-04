"""
Unit Test for two_sum_data_structure
"""
from unittest import TestCase

from problems.array.two_sum_data_structure import TwoSumDataStructure


class TestTwoSumDataStructure(TestCase):
    """
    Unit test for TwoSumDataStructure
    """

    def test_find(self):
        """Test find

        Args:
            self: TestTwoSumDataStructure

        Returns:
            None

        Raises:
            None
        """
        # Given
        two_sum_problem = TwoSumDataStructure()
        two_sum_problem.add(2)
        two_sum_problem.add(6)
        two_sum_problem.add(7)
        two_sum_problem.add(5)
        two_sum_problem.add(8)
        two_sum_problem.add(9)

        # Then
        self.assertTrue(two_sum_problem.find(8))
        self.assertTrue(two_sum_problem.find(9))
        self.assertTrue(two_sum_problem.find(7))
        self.assertTrue(two_sum_problem.find(10))
        self.assertTrue(two_sum_problem.find(11))
        self.assertTrue(two_sum_problem.find(12))
        self.assertTrue(two_sum_problem.find(13))
        self.assertTrue(two_sum_problem.find(14))
        self.assertTrue(two_sum_problem.find(15))
        self.assertTrue(two_sum_problem.find(16))
        self.assertTrue(two_sum_problem.find(17))
