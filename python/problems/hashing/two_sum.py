"""
Two Sum

Given an array of integers, find two numbers such that they add up to a specific target
number.

The function twoSum should return indices of the two numbers such that they add up to
the target, where index1 must be less than index2. Please note that your returned answers
(both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.
"""
from common.problem import Problem


class TwoSum(Problem):
    """
    Two Sum
    """
    PROBLEM_NAME = "TwoSum"

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

        Note: The O(n) runtime uses the commutative property of addition.
        (target_sum-x) is searched for in the given map. However, it takes O(n) extra space for the dictionary.
        Comparatively, O(n^2) brute-force solution adds each element with every other element.

        Args:

        Returns:
            tuple

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        input_dict = {}
        for i in range(0, len(self.input_list)):
            x = self.input_list[i]

            if (self.target_sum - x) in input_dict:
                return input_dict[self.target_sum - x] + 1, i + 1

            input_dict[x] = i

        assert (False, "InvalidArguments")
