"""
Sort By Color

Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: Using library sort function is not allowed.

Example :

Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
"""
from common.problem import Problem


class SortByColor(Problem):
    """
    Sort By Color
    """
    PROBLEM_NAME = "SortByColor"

    def __init__(self, input_list):
        """Sort By Color

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

        Note:

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        low = 0
        mid = 0
        high = len(self.input_list) - 1

        while mid <= high:
            if self.input_list[mid] == 0:
                self.input_list[low], self.input_list[mid] = self.input_list[mid], self.input_list[low]
                low = low + 1
                mid = mid + 1
            elif self.input_list[mid] == 1:
                mid = mid + 1
            else:
                self.input_list[mid], self.input_list[high] = self.input_list[high], self.input_list[mid]
                high = high - 1

        return self.input_list
