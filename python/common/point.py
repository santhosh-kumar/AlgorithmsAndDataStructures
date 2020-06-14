"""
This module defines a point data structure
"""


class Point2D:
    """
    An implementation of point.
    """

    def __init__(self, x, y):
        """__init__

        Args:
            x: coordinate
            y: coordinate

        Returns:
            None

        Raises:
            None
        """
        self.x = x
        self.y = y

    def get(self):
        """get

        Args:

        Returns:
            tuple

        Raises:
            None
        """
        return self.x, self.y

    @staticmethod
    def orientation(point1, point2, point3):
        """Returns the orientation

        Args:
            point1: First point
            point2: Second point
            point3: Third point

        Returns:
            # 0 : Collinear points
            # 1 : Clockwise points
            # 2 : Counterclockwise

        Raises:
            None
        """
        # (y2-y1) * (x3-x2) - (x2-x1) * (y3-y2)
        val = (float(point2.y - point1.y) * (point3.x - point2.x)) - \
              (float(point2.x - point1.x) * (point3.y - point2.y))

        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2
