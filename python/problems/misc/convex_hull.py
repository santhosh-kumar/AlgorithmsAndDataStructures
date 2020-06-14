"""
Convex Hull

Given a set of points in the plane. the convex hull of the set is the smallest convex polygon
that contains all the points of it.

"""
from common.point import Point2D
from common.problem import Problem


class ConvexHull(Problem):
    """
    ConvexHull
    """
    PROBLEM_NAME = "ConvexHull"

    def __init__(self, input_points_list):
        """Convex Hull

        Args:
            input_points_list: List of points

        Returns:
            list

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_points_list = input_points_list

    def solve(self):
        """Solve the problem

        Note:  For every point on the hull we examine all the other points to determine the next point.
        Time complexity is ?(m * n) where n is number of input points and m is number of output or hull points (m <= n).
        In worst case, time complexity is O(n 2). The worst case occurs when all the points are on the hull (m = n)

        Args:

        Returns:
            string

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        convex_hull = []

        # There should be at least 3 points to make a convex hull
        if len(self.input_points_list) < 3:
            return convex_hull

        left_index = self.left_most_index(self.input_points_list)

        ''' 
        Start from leftmost point, keep moving counterclockwise  
        until reach the start point again. This loop runs O(h)  
        times where h is number of points in result or output.  
        '''
        p = left_index
        q = 0
        n = len(self.input_points_list)

        while True:
            # Add the current point to the list
            convex_hull.append(self.input_points_list[p].get())

            ''' 
            Search for a point 'q' such that orientation(p, x,  
            q) is counterclockwise for all points 'x'. The idea  
            is to keep track of last visited most counterclock-  
            wise point in q. If any point 'i' is more counterclock-  
            wise than q, then update q.  
            '''
            q = (p + 1) % n

            for i in range(n):
                # If i is more counterclockwise
                # than current q, then update q
                if (Point2D.orientation(self.input_points_list[p], self.input_points_list[i],
                                        self.input_points_list[q]) == 2):
                    q = i

            ''' 
            Now q is the most counterclockwise with respect to p  
            Set p as q for next iteration, so that q is added to  
            result 'hull'  
            '''
            p = q

            # While we don't come to first point
            if p == left_index:
                break

        return convex_hull

    @staticmethod
    def left_most_index(points_list):
        """Return the left most index

        Args:

        Returns:
            integer

        Raises:
            None
        """
        left_index = 0

        for i in range(1, len(points_list)):
            if points_list[i].x < points_list[left_index].x:
                left_index = i
            elif points_list[i].x == points_list[left_index] and points_list[i].y > points_list[left_index].y:
                left_index = i

        return left_index
