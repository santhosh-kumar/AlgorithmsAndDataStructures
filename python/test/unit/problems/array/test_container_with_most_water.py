"""
Unit Test for container_with_most_water
"""
from unittest import TestCase

from problems.array.container_with_most_water import ContainerWithMostWater


class TestContainerWithMostWater(TestCase):
    """
    Unit test for ContainerWithMostWater
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestContainerWithMostWater

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [1, 5, 4, 3]
        most_water_problem = ContainerWithMostWater(input_list)

        # When
        result = most_water_problem.solve()

        # Then
        self.assertEqual(result, 6)
