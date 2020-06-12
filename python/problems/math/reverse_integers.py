"""
Reverse Integers

Reverse digits of an integer. For example: x = 123, return 321."abc"  false

Q: What about negative integers?
A: For input x = –123, you should return –321.

Q: What if the integer’s last digit is 0? For example, x = 10, 100, …
A: Ignore the leading 0 digits of the reversed integer. 10 and 100 are both reversed as 1.

Q: What if the reversed integer overflows? For example, input x = 1000000003.
A: In this case, your function should return 0.
"""
from common.problem import Problem


class ReverseIntegers(Problem):
    """
    ReverseIntegers
    """
    PROBLEM_NAME = "ReverseIntegers"
    MAX_INT_SIZE = 2147483647

    def __init__(self, input_integer):
        """Reverse Integers

        Args:
            input_integer: input_integer to be reversed

        Returns:
            None

        Raises:
            None
        """
        assert isinstance(input_integer, int), "Invalid input type -- int expected"
        super().__init__(self.PROBLEM_NAME)
        self.input_integer = int(input_integer)

    def solve(self):
        """Solve the problem

        Note: O(n) (runtime) and O(1) (space) solution works by using the modulo operator to get the last digit of the number.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        sign = 1
        if self.input_integer < 0:
            sign = -1
            self.input_integer = abs(self.input_integer)

        reversed_integer = 0
        while self.input_integer != 0:
            reversed_integer = reversed_integer * 10 + self.input_integer % 10
            self.input_integer = int(self.input_integer / 10)

            if abs(reversed_integer) > self.MAX_INT_SIZE:
                return 0

        return sign * reversed_integer
