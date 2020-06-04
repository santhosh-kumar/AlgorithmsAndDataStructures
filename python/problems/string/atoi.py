"""
AtoI

Implement atoi to convert a string to an integer.

The atoi function first discards as many whitespace characters as necessary until the first
non-whitespace character is found. Then, starting from this character, takes an optional
initial plus or minus sign followed by as many numerical digits as possible, and interprets
them as a numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or
if no such sequence exists because either str is empty or it contains only whitespace
characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

If the correct value is out of the range of representable values, the maximum integer value (2147483647) or the
minimum integer value (–2147483648) is returned.
"""
import string

from common.problem import Problem


class AtoI(Problem):
    """
    TwoSum
    """
    PROBLEM_NAME = "AtoI"
    PLUS_SIGN = '+'
    MINUS_SIGN = '-'
    MAX_INT_VALUE = 2147483647
    MIN_INT_VALUE = -2147483647

    def __init__(self, input_string):
        """AtoI

        Args:
            input_string: contains the input string
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_string = input_string

    def solve(self):
        """Solve the problem
        Note: O(n) solution works by iterating over the string to skip leading spaces and then looks for sign.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        if len(self.input_string) == 0:
            return 0

        number = 0
        i = 0

        # process the leading spaces
        while self.input_string[i] == " " and i < len(self.input_string):
            i = i + 1

        # process the sign (if available)
        sign = 1
        if self.input_string[i] == self.MINUS_SIGN:
            sign = -1
            i = i + 1
        elif self.input_string[i] == self.PLUS_SIGN:
            i = i + 1

        while i < len(self.input_string):
            if self.input_string[i] in string.digits:
                number = number * 10 + int(self.input_string[i])
            else:
                assert (False, "Invalid character for conversion")

            if (number * sign) > self.MAX_INT_VALUE:
                return self.MAX_INT_VALUE
            elif (number * sign) < self.MIN_INT_VALUE:
                return self.MIN_INT_VALUE

            i = i + 1

        return sign * number
