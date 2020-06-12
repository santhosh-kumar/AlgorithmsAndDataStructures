"""
Single Number

Given an array of integers, every element appears twice except for one. Find that single
one.
"""
from common.problem import Problem


class SingleNumber(Problem):
    """
    Single Number
    """
    PROBLEM_NAME = "SingleNumber"

    def __init__(self, input_list):
        """Single Number

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
            i. We can have a map to count the number of times an element occurs. The lookup on map is O(1), the total
            runtime complexity is O(n) and the space complexity is O(n) (due to an additional map). However, it takes two passes
            to find the solution.

            ii. For an one pass solution, XOR all the numbers in an array. If the number occurs twice, it will cancel out. Otherwise, the single
            number would remain at the end. This assumes numbers are greater than 0 and only one number has the single occurrence.

        Note:

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        single_number = 0
        for i in range(len(self.input_list)):
            single_number = single_number ^ self.input_list[i]

        return single_number
