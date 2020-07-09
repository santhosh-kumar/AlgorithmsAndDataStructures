"""
Container With Most Water

Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Your program should return an integer which corresponds to the maximum area of water that can be contained
( Yes, we know maximum area instead of maximum volume sounds weird. But this is 2D plane we are working with for simplicity ).

Note: You may not slant the container.
Example :

Input : [1, 5, 4, 3]
Output : 6

Explanation : 5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3.
So total area = 3 * 2 = 6
"""
from common.problem import Problem


class ContainerWithMostWater(Problem):
    """
    Container With Most Water
    """
    PROBLEM_NAME = "ContainerWithMostWater"

    def __init__(self, input_list):
        """ContainerWithMostWater

        Args:
            input_list: Contains a list of integers

        Returns:
            None

        Raises:
            None
        """
        assert (len(input_list) > 0)

        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list

    def solve(self):
        """Solve the problem

        Note: O(n) (runtime) and O(1) (space)

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        left = 0
        right = len(self.input_list) - 1
        area = 0

        while left < right:
            area = max(area, min(self.input_list[left], self.input_list[right]) * (right - left))

            if self.input_list[left] < self.input_list[right]:
                left = left + 1
            else:
                right = right - 1

        return area
