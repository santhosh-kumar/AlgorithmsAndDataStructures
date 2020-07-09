"""
Largest Rectangle in Histogram

Given an array of integers A of size N. A represents a histogram i.e A[i] denotes height of
the ith histogram’s bar. Width of each bar is 1.

Find the area of largest rectangle in the histogram.

Input 1:
    A = [2, 1, 5, 6, 2, 3]
Output 1:
    10
Explanation 1:
    The largest rectangle is shown in the shaded area, which has area = 10 unit.
"""
from common.problem import Problem
from common.stack import Stack


class LargestRectangleInHistogram(Problem):
    """
    LargestRectangleInHistogram
    """
    PROBLEM_NAME = "LargestRectangleInHistogram"

    def __init__(self, input_list):
        """LargestRectangleInHistogram

        Args:
            input_list: histogram entries as a list

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list

    def solve(self):
        """Solve the problem

        Note: O(n) (runtime) since every bar is pushed and popped only once.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        # stack to store the indices
        stack = Stack()

        max_area = 0
        index = 0

        while index < len(self.input_list):
            # If this bar is higher than the bar on top stack, push it to stack
            if len(stack) == 0 or self.input_list[stack.peek()] <= self.input_list[index]:
                stack.push(index)
                index = index + 1

            # If this bar is lower than top of stack, then calculate area of rectangle with
            # stack top as the smallest (or minimum # height) bar.'i' is 'right index' for
            # the top and element before top in stack is 'left index'
            else:
                top_index = stack.pop()

                # Calculate the area with histogram[top_of_stack] stack as smallest bar
                area = (self.input_list[top_index] * ((index - stack.peek() - 1) if stack else index))

                max_area = max(area, max_area)

        # Now pop the remaining bars from  stack and calculate area with
        # every popped bar as the smallest bar
        while stack:
            # pop the top
            top_index = stack.pop()

            # Calculate the area with
            # histogram[top_of_stack]
            # stack as smallest bar
            area = (self.input_list[top_index] * ((index - stack.peek() - 1) if stack else index))

            # update max area, if needed
            max_area = max(max_area, area)

        return max_area
