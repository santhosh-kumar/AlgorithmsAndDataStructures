"""
Max of SubArray of Size K

Given an array A and an integer K.
Find the maximum sum subarray of size K.

You may assume that each input would have exactly one solution.
"""
from collections import deque

from common.problem import Problem


class MaxOfSubArrayWithSize(Problem):
    """
    MaxOfSubArrayWithSize
    """
    PROBLEM_NAME = "MaxOfSubArrayWithSize"

    def __init__(self, input_list, size):
        """MaxOfSubArrayWithSize

        Args:
            input_list: Contains a list of integers
            size: size of the subarray

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list
        self.size = size

    def solve(self):
        """Solve the problem

        Note: O(n) (runtime) and O(k) (space) solution uses a stack to store the subarray that is seen so far.

        Args:

        Returns:
            tuple

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        subarray_queue = deque()

        result = []
        for i in range(len(self.input_list)):
            if len(subarray_queue) >= self.size:
                result.append(sum(subarray_queue))
                subarray_queue.popleft()

            subarray_queue.append(self.input_list[i])

        result.append(sum(subarray_queue))

        return max(result)
