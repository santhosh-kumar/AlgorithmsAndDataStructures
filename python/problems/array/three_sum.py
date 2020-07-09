"""
Three Sum

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution

Example:
given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
"""
import sys

from common.problem import Problem


class ThreeSum(Problem):
    """
    Three Sum
    """
    PROBLEM_NAME = "ThreeSum"

    def __init__(self, input_list, target_sum):
        """Two Sum

        Args:
            input_list: Contains a list of integers
            target_sum: Target sum for which the indices need to be returned

        Returns:
            None

        Raises:
            None
        """
        assert (len(input_list) > 0)
        assert (target_sum > 0)

        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list
        self.target_sum = target_sum

    def solve(self):
        """Solve the problem

        Note: There are only two nested loops traversing the array, so time complexity is O(n^2).
        Two pointer algorithm take O(n) time and the first element can be fixed using another nested traversal.
        The space complexity is O(1).

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        # sort the array
        self.input_list.sort()

        closest_sum = sys.maxsize

        for i in range(len(self.input_list) - 2):
            ptr1 = i + 1
            ptr2 = len(self.input_list) - 1

            while ptr1 < ptr2:
                total = self.input_list[i] + self.input_list[ptr1] + self.input_list[ptr2]

                if abs(self.target_sum - total) < abs(self.target_sum - closest_sum):
                    closest_sum = total

                if total > self.target_sum:
                    ptr2 = ptr2 - 1
                else:
                    ptr1 = ptr1 + 1

        return closest_sum
