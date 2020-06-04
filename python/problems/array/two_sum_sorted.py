"""
Two Sum (sorted)

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Assume input array is sorted in ascending order.
"""
from common.problem import Problem


class TwoSumSorted(Problem):
    """
    TwoSumSorted
    """
    PROBLEM_NAME = "TwoSumSorted"
    NOT_FOUND = -1

    def __init__(self, input_list, target_sum):
        """Two Sum Sorted

        The O(n * logn) runtime uses the fact that the array is already sorted.
        (target_sum-x) is binary searched in the input_list between current_index+1 and the length of the array. However, it takes O(1) space.

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

        for i in range(0, len(self.input_list)):
            x = self.input_list[i]
            found_index = self.binary_search((self.target_sum - x), i + 1)
            if found_index > self.NOT_FOUND:
                return found_index, found_index + 1
        assert (False, "InvalidArguments")

    def binary_search(self, key, start_index):
        """binary searches a given key
        Args:
            key: search key
            start_index: starting index for searching (bounded by the length of the array)
        Returns:
            None

        Raises:
            None
        """
        assert (start_index > self.NOT_FOUND)

        left_index = start_index
        right_index = len(self.input_list) - 1

        while left_index < right_index:
            middle_index = int((left_index + right_index) / 2)
            if self.input_list[middle_index] < key:
                left_index = middle_index + 1
            else:
                right_index = middle_index

        if left_index == right_index and self.input_list[middle_index] == key:
            return middle_index
        else:
            return self.NOT_FOUND
