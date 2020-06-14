"""
Maximum Subarray XOR

Given an array of integers. find the maximum XOR subarray value in given array. Expected time complexity O(n).

Examples:

Input: arr[] = {1, 2, 3, 4}
Output: 7
The subarray {3, 4} has maximum XOR value

Input: arr[] = {8, 1, 2, 12, 7, 6}
Output: 15
The subarray {1, 2, 12} has maximum XOR value

Input: arr[] = {4, 6}
Output: 6
The subarray {6} has maximum XOR value
"""
import sys

from common.problem import Problem


class MaxSubarrayXOR(Problem):
    """
    Maximum Subarray XOR
    """
    PROBLEM_NAME = "MaxSubarrayXOR"

    def __init__(self, input_list):
        """Two Sum

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

        Note: O(n^2) (runtime) solution works by leaving n (0...N) items at a time and computing XOR among the rest.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        result = -sys.maxsize

        # Pick starting points of subarrays
        for i in range(len(self.input_list)):
            current_xor = 0

            # Pick ending points of subarrays starting with i
            for j in range(i, len(self.input_list)):
                current_xor = current_xor ^ self.input_list[j]
                result = max(result, current_xor)

        return result
