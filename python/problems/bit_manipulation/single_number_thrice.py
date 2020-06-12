"""
Single Number Thrice

Given an array of integers, every element appears three times except for one. Find that
single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without
using extra memory?
"""
from common.problem import Problem


class SingleNumberThrice(Problem):
    """
    Single Number Thrice
    """
    PROBLEM_NAME = "SingleNumberThrice"

    def __init__(self, input_list):
        """Single Number Thrice

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
        Note: O(n) (runtime) and O(1) (space) solution works by counting number of occurrences of elements in array
            i.e., ones, twos and threes. Finally, print the ones.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        ones = 0
        twos = 0
        for i in range(len(self.input_list)):
            # if the ones is already set, twos will be set
            twos = twos | (ones & self.input_list[i])

            # XOR find if the element occurs once
            ones = ones ^ self.input_list[i]

            # should be both twos and ones
            threes = twos & ones

            # appeared once and not thrice
            ones = ones & ~ threes

            # appeared twice and not thrice
            twos = twos & ~ threes

        return ones
