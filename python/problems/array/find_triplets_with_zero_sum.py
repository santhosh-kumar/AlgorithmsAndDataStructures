"""
Find Triplets with Zero Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2)
"""

from common.problem import Problem


class FindTripletsWithZeroSum(Problem):
    """
    Find Triplets With Zero Sum
    """
    PROBLEM_NAME = "FindTripletsWithZeroSum"

    def __init__(self, input_list):
        """FindTripletsWithZeroSum

        Args:
            input_list: Contains a list of integers

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list

    def solve(self):
        """Solve the problem

        Note: O(n^2) (runtime) and O(n) (space) sorts the array and requires only two nested loops.

        Args:

        Returns:
            list(list)

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        n = len(self.input_list)

        self.input_list.sort()

        result = []
        for i in range(0, n - 1):
            left = i + 1
            right = n - 1
            x = self.input_list[i]
            while left < right:
                if x + self.input_list[left] + self.input_list[right] == 0:
                    result.append([x, self.input_list[left], self.input_list[right]])
                    left = left + 1
                    right = right - 1

                elif (x + self.input_list[left] + self.input_list[right]) < 0:
                    left = left + 1

                else:
                    right = right - 1

        return result
