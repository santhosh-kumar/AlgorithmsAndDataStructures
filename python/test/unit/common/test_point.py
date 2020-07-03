"""
Unit Test for point
"""
from unittest import TestCase

from common.point import Point2D


class TestPoint2D(TestCase):
    """
    Unit test for Point2D
    """

    def test_orientation(self):
        """Test for get_orientation

        Args:
            self: TestPoint2D

        Returns:
            None

        Raises:
            None
        """
        # Given
        point1 = Point2D(0, 0)
        point2 = Point2D(0, 1)
        point3 = Point2D(0, 2)
        point4 = Point2D(1, 1)

        # Then
        self.assertEqual(Point2D.orientation(point1, point2, point3), 0)  # collinear
        self.assertEqual(Point2D.orientation(point3, point4, point2), 1)  # clockwise
        self.assertEqual(Point2D.orientation(point2, point4, point3), 2)  # counter-clockwise
