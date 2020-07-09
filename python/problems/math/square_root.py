"""
Square Root of an Integer (using binary search)

Given an integer x, find it’s square root. If x is not a perfect square, then return floor(√x).

Examples :

Input: x = 4
Output: 2
Explanation:  The square root of 4 is 2.

Input: x = 11
Output: 3
Explanation:  The square root of 11 lies in between
3 and 4 so floor of the square root is 3.
"""
from common.problem import Problem


class SquareRoot(Problem):
    """
    Square Root of an Integer
    """
    PROBLEM_NAME = "SquareRoot"

    def __init__(self, input_number):
        """Square Root of an Integer

        Args:
            input_number: input_number

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_number = input_number

    def solve(self):
        """Solve the problem

        Note: O(logn) (runtime) and O(1) (space) solution works by exploiting the binary search.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if self.input_number == 0 or self.input_number == 1:
            return self.input_number

        start = 1
        end = self.input_number

        result = None

        while start <= end:
            middle = (start + end) // 2

            # If x is a perfect square
            if middle * middle == self.input_number:
                return middle

            # Since we need floor, we update
            # answer when mid*mid is smaller
            # than x, and move closer to sqrt(x)
            if middle * middle < self.input_number:
                start = middle + 1
                result = middle
            else:
                # If middle * middle is greater than x
                end = middle - 1

        return result
