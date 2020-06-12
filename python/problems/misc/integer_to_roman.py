"""
Integer to Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

Hint:
What is the range of the numbers?
"""
from common.problem import Problem


class IntegerToRoman(Problem):
    """
    IntegerToRoman
    """
    PROBLEM_NAME = "IntegerToRoman"

    INTEGER_VALUES = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    ROMAN_SYMBOLS = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    def __init__(self, input_integer):
        """Integer to roman

        Args:
            input_integer: input_integer to be converted to roman numerals

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
        Note: O(n) solution works by dividing the integer from the highest element in the range and subtracting iteratively till the number becomes zero.

        Args:

        Returns:
            string

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        i = 0
        number = self.input_integer
        roman_numerals = ""

        while number > 0:
            k = int(number / self.INTEGER_VALUES[i])

            for j in range(k):
                roman_numerals = roman_numerals + self.ROMAN_SYMBOLS[i]
                number = number - self.INTEGER_VALUES[i]

            i = i + 1

        return roman_numerals
