"""
Find Min In Sorted Rotated Array (with duplicates)

If the rotated sorted array could contain duplicates? Is your algorithm still O(log n) in
runtime complexity?
"""
from common.problem import Problem


class FindMinInSortedRotatedArrayWithDuplicates(Problem):
    """
    Find Min In Sorted Rotated Array (with duplicates)
    """
    PROBLEM_NAME = "FindMinInSortedRotatedArrayWithDuplicates"

    def __init__(self, input_list):
        """Find Min In Sorted Rotated Array (with duplicates)

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

        Note:  For case where AL == AM == AR, the minimum could be on AM’s left or right side (eg,
        [1, 1, 1, 0, 1] or [1, 0, 1, 1, 1]). In this case, we could not discard either subarrays and
        therefore such worst case degenerates to the order of O(n).

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
            elif self.input_list[middle] < self.input_list[left]:
                right = middle
            else:
                left = left + 1

        return self.input_list[left]
