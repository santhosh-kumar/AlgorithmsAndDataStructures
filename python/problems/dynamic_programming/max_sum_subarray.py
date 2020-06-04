"""
Max Sum SubArray

Find the contiguous sub-array within an array (containing at least one number) that has the
largest sum.

For example, given the array [2, 1, –3, 4, –1, 2, 1, –5, 4],

The contiguous array [4, –1, 2, 1] has the largest sum = 6.
"""
from common.problem import Problem


class MaxSumSubArray(Problem):
    """
    Max Sum SubArray
    """
    PROBLEM_NAME = "MaxSumSubArray"

    def __init__(self, input_list):
        """Max Sum SubArray

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

        Note: O(n) (runtime) and O(1) (space) solution calculates the maximum till the last element plus current element or the current element.
        It updates the maximum seen so far based on the computation.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if len(self.input_list) == 0:
            return 0

        max_so_far = self.input_list[0]
        current_max_ending = 0

        for i in range(1, len(self.input_list)):
            current_max_ending = max(current_max_ending + self.input_list[i], self.input_list[i])
            max_so_far = max(max_so_far, current_max_ending)

        return max_so_far
