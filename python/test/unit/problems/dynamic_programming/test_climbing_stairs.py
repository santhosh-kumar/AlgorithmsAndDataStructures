"""
Unit Test for climbing_stairs
"""
from unittest import TestCase

from problems.dynamic_programming.climbing_stairs import ClimbingStairs


class TestClimbingStairs(TestCase):
    """
    Unit test for ClimbingStairs
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestClimbingStairs

        Returns:
            None

        Raises:
            None
        """
        # Given
        number_steps = 4
        climbing_stairs_problem = ClimbingStairs(number_steps)

        # When
        number_ways = climbing_stairs_problem.solve()

        # Then
        self.assertEqual(number_ways, 5)
