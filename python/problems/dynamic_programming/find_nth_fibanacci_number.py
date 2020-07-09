"""
Find nth Fibanacci Number

The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation

    Fn = Fn-1 + Fn-2

with seed values

   F0 = 0 and F1 = 1.
"""
from common.problem import Problem


class FindNthFibanacciNumber(Problem):
    """
    Find nth Fibanacci Number
    """
    PROBLEM_NAME = "FindNthFibanacciNumber"

    def __init__(self, n):
        """Find nth Fibanacci Number

        Args:
            n: nth number to find
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.n = n

    def solve(self):
        """Solve the problem

        Note: O(n) (runtime) and O(1) (space) solution works by storing the previous two values.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        a = 0
        b = 1

        if self.n == 0:
            return a
        elif self.n == 1:
            return b
        else:
            for i in range(2, self.n + 1):
                c = a + b
                a = b
                b = c

            return b
