"""
Greatest Common Divisor (Euclid Method)

Greatest common divisor(GCD) of two integers X and Y is the largest integer that divides both X and Y.
"""
from common.problem import Problem


class GreatestCommonDivisor(Problem):
    """
    GreatestCommonDivisor
    """
    PROBLEM_NAME = "GreatestCommonDivisor"

    def __init__(self, input_number1, input_number2):
        """Greatest Common Divisor

        Args:
            input_number1: First number
            input_number2: Second number

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_number1 = input_number1
        self.input_number2 = input_number2

    def solve(self):
        """Solve the problem

        Note: O(n) (runtime) complexity.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        return self.get_gcd(self.input_number1, self.input_number2)

    @staticmethod
    def get_gcd(number1, number2):
        """Get gcd recursively

        Args:
            number1: First number
            number2: Second number

        Returns:
            integer

        Raises:
            None
        """
        if number2 == 0:
            return number1
        else:
            return GreatestCommonDivisor.get_gcd(number2, number1 % number2)
