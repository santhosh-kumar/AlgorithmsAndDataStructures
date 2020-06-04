"""
Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

"""
from common.problem import Problem


class RomanToInteger(Problem):
    """
    Roman To Integer
    """
    PROBLEM_NAME = "RomanToInteger"

    ROMAN_NUMERALS_MAP = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __init__(self, input_roman_numerals):
        """Roman to Integer

        Args:
            input_roman_numerals: input_roman_numerals to be converted to an integer

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_roman_numerals = input_roman_numerals

    def solve(self):
        """Solve the problem

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        previous = 0
        total = 0

        for c in self.input_roman_numerals:
            current = self.ROMAN_NUMERALS_MAP[c]

            if current > previous:
                total = total + (current - 2 * previous)
            else:
                total = total + current

            previous = current

        return total
