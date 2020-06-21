"""
This module defines the quad tree data structure

A quadtree is a data structure that can be useful for spatial indexing (it's often used in games for collision detection).
In a quadtree, each node has exactly 4 children. When the number of nodes in a leaf reaches a specified threshold,
the tree recursively divides.
"""
from common.point import Point2D


class QuadTreeNode:
    """
    A node in QuadTree
    """

    def __init__(self, x0, y0, width, height, points):
        """init QuadTree
        Args:
            x0: X-value
            y0: Y-value
            width: of the grid
            height: of the grid
            points: in the grid
        Returns:
            None

        Raises:
            None
        """
        self.x0 = x0
        self.y0 = y0
        self.width = width
        self.height = height
        self.points = points
        self.children = []


class QuadTree:
    """
    An implementation of QuadTree
    """

    def __init__(self, threshold):
        """init QuadTree
        Args:
            threshold: Number of points allowed in a grid

        Returns:
            None

        Raises:
            None
        """
        self.threshold = threshold
        self.points = []
        self.root = QuadTreeNode(0, 0, 10, 10, self.points)

    def add_point(self, x, y):
        """Add a point
        Args:
            x: x-location
            y: y-location

        Returns:
            None

        Raises:
            None
        """
        self.points.append(Point2D(x, y))
        self.subdivide()

    def subdivide(self):
        """Subdivide
        Args:

        Returns:
            None

        Raises:
            None
        """
        self.subdivide_util(self.root, self.threshold)

    @staticmethod
    def subdivide_util(node, threshold):
        """Subdivide (if number of points exceeds the threshold)
        Args:
            node: root node
            threshold: Max allowed points

        Returns:
            None

        Raises:
            None
        """
        if len(node.points) <= threshold:
            return

        half_width = float(node.width / 2)
        half_height = float(node.height / 2)
        quadrants = [(node.x0, node.y0), (node.x0, node.y0 + half_height), (node.x0 + half_width, node.y0),
                     (node.x0 + half_width, node.y0 + half_height)]

        quadrant_nodes = []
        for quadrant in quadrants:
            contained_points = QuadTree.contains(quadrant[0], quadrant[1], half_width, half_height, node.points)
            quadrant_node = QuadTreeNode(quadrant[0], quadrant[1], half_width, half_height, contained_points)
            quadrant_nodes.append(quadrant_node)
            QuadTree.subdivide_util(quadrant_node, threshold)

        node.children = quadrant_nodes

    @staticmethod
    def contains(x, y, width, height, points):
        """contains
        Args:
            x: X-value
            y: Y-value
            width: of the grid
            height: of the grid
            points: in the grid

        Returns:
            None

        Raises:
            None
        """
        contained_points = []
        for point in points:
            if x <= point.x <= x + width and y <= point.y <= y + height:
                contained_points.append(point)

        return contained_points

    @staticmethod
    def find_children(node):
        if not node.children:
            return [node]
        else:
            children = []
            for child in node.children:
                children += (QuadTree.find_children(child))
        return children
