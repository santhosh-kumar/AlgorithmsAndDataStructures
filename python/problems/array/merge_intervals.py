"""
Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6]
.
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
from common.problem import Problem


class MergeIntervals(Problem):
    """
    Merge Intervals
    """
    PROBLEM_NAME = "MergeIntervals"

    def __init__(self, input_range_list1, input_range_list2):
        """Merge Intervals

        Args:
            input_range_list1: First range list
            input_range_list2: First range list

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_range_list1 = input_range_list1
        self.input_range_list2 = input_range_list2

    def solve(self):
        """Solve the problem

        Note: O(n logn) (runtime) and O(1) (space) works by combining the list and sorting in O(n logn). Then, the combined
        list traversed in O(n) and comparing the last value of the interval with the last value in the currently merged list.

        Args:

        Returns:
            list(list)

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        merged_list = []

        interval_list = sorted(self.input_range_list1 + self.input_range_list2, key=lambda x: x[0])

        for interval in interval_list:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged_list or merged_list[-1][1] < interval[0]:
                merged_list.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged_list[-1][1] = max(merged_list[-1][1], interval[1])

        return merged_list
