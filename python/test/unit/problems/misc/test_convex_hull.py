"""
Unit Test for convex_hull
"""
from unittest import TestCase

from common.point import Point2D
from problems.misc.convex_hull import ConvexHull


class TestConvexHull(TestCase):
    """
    Unit test for ConvexHull
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestConvexHull

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_points_list = []
        input_points_list.append(Point2D(0, 3))
        input_points_list.append(Point2D(2, 2))
        input_points_list.append(Point2D(1, 1))
        input_points_list.append(Point2D(2, 1))
        input_points_list.append(Point2D(3, 0))
        input_points_list.append(Point2D(0, 0))
        input_points_list.append(Point2D(3, 3))

        convex_hull_problem = ConvexHull(input_points_list)

        # When
        convex_hull = convex_hull_problem.solve()

        # Then
        self.assertEqual(convex_hull, [(0, 3), (0, 0), (3, 0), (3, 3)])
