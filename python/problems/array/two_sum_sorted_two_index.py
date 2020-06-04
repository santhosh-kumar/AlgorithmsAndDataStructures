"""
Two Sum (sorted) -- two index solution

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Assume input array is sorted in ascending order.
"""
from common.problem import Problem


class TwoSumSortedTwoIndex(Problem):
    """
    TwoSumSortedTwoIndex
    """
    PROBLEM_NAME = "TwoSumSortedTwoIndex"
    NOT_FOUND = -1

    def __init__(self, input_list, target_sum):
        """Two Sum Sorted -- Two Indices solution

        Note: The O(n) runtime uses the fact that the array is already sorted and it takes O(1) space by comparing sum of the elements to adjust the left and right indices.
        if sum is lesser than target, the left index is increased. Otherwise, the right index is decreased.

        Args:
            input_list: Contains a list of integers (sorted ascending order)
            target_sum: Target sum for which the indices need to be returned
        Returns:
            None0

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
        Args:

        Returns:
            tuple

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        left_index = 0
        right_index = len(self.input_list) - 1

        while left_index < right_index:
            sum_index_values = self.input_list[left_index] + self.input_list[right_index]
            if sum_index_values < self.target_sum:
                left_index = left_index + 1
            elif sum_index_values > self.target_sum:
                right_index = right_index - 1
            else:
                return left_index + 1, right_index + 1

        assert (False, "InvalidArguments")
