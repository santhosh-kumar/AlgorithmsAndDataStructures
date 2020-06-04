"""
Unit Test for plus_one
"""
from unittest import TestCase

from problems.math.plus_one import PlusOne


class TestPlusOne(TestCase):
    """
    Unit test for PlusOne
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestPlusOne

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_integers_list = [9, 9, 9]
        plus_one_problem = PlusOne(input_integers_list)

        # When
        result = plus_one_problem.solve()

        # Then
        self.assertEqual(result, [1, 0, 0, 0])
