"""
Longest Increasing Subsequence

Find the longest increasing subsequence of a given array of integers, A.

Input 1:
    A = [1, 2, 1, 5]

Output 1:
    3

Explanation 1:
    The sequence : [1, 2, 5]

Input 2:
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

Output 2:
    6

Explanation 2:
    The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]
"""
from common.problem import Problem


class LongestIncreasingSubsequence(Problem):
    """
    LongestIncreasingSubsequence
    """
    PROBLEM_NAME = "LongestIncreasingSubsequence"
    NOT_FOUND = -1

    def __init__(self, input_list):
        """LongestIncreasingSubsequence

        Args:
            input_list: List of integers

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list

    def solve(self):
        """Solve the problem
        Args:

        Note: O(n^2) (runtime) and O(1) (space) using dynamic programming.

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        n = len(self.input_list)

        lis_array = [1] * n

        # Compute optimized LIS values in bottom up manner
        for i in range(1, n):
            for j in range(0, i):
                if self.input_list[i] > self.input_list[j] and lis_array[i] < lis_array[j] + 1:
                    lis_array[i] = lis_array[j] + 1

        # Pick maximum of all LIS values
        return max(lis_array)
