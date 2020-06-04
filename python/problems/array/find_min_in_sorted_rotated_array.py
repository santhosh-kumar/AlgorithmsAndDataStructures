"""
Find Min In Sorted Rotated Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""
from common.problem import Problem


class FindMinInSortedRotatedArray(Problem):
    """
    Find Min In Sorted Rotated Array
    """
    PROBLEM_NAME = "FindMinInSortedRotatedArray"

    def __init__(self, input_list):
        """Find Min In Sorted Rotated Array

        Args:
            input_list: Contains a list of integers (sorted)
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list

    def solve(self):
        """Solve the problem

        Note: O(log n) (runtime) solution works by comparing the middle element with the right most element.
        Then adjusting the left and right indices.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        left = 0
        right = len(self.input_list) - 1

        while left < right and self.input_list[left] > self.input_list[right]:
            middle = int((left + right) / 2)
            if self.input_list[middle] > self.input_list[right]:
                left = middle + 1
            else:
                right = middle

        return self.input_list[left]
