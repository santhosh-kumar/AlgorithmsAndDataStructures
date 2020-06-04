"""
Valid Number

Validate if a given string is numeric.

Some examples:
"0"  true
"0.1"  true
"abc"  false

Q: How to account for whitespaces in the string?
A: When deciding if a string is numeric, ignore both leading and trailing whitespaces.

Q: Should I ignore spaces in between numbers – such as “1 1”?
A: No, only ignore leading and trailing whitespaces. “1 1” is not numeric.

Q: If the string contains additional characters after a number, is it considered valid?
A: No. If the string contains any non-numeric characters (excluding whitespaces and decimal
point), it is not numeric.

Q: Is it valid if a plus or minus sign appear before the number?
A: Yes. “+1” and “-1” are both numeric.

Q: Should I consider only numbers in decimal? How about numbers in other bases such as
hexadecimal (0xFF)?
A: Only consider decimal numbers. “0xFF” is not numeric.

Q: Should I consider exponent such as “1e10” as numeric?
A: No. But feel free to work on the challenge that takes exponent into consideration. (The Online
Judge problem does take exponent into account.)

"""
import string

from common.problem import Problem


class ValidNumber(Problem):
    """
    ValidNumber
    """
    PROBLEM_NAME = "ValidNumber"
    DECIMAL_SIGN = "."
    PLUS_SIGN = '+'
    MINUS_SIGN = '-'

    def __init__(self, input_string):
        """Valid Number

        Args:
            input_string: input_string to be checked if it's a number
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_string = input_string

    def solve(self):
        """Solve the problem

        Note: O(n) works by iterating by iterating the string and skipping the leading spaces.
        Then, accommodating signs, digits and decimal.

        Args:

        Returns:
            boolean

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if len(self.input_string) == 0:
            return False

        i = 0

        # process the leading spaces
        while self.input_string[i] == " " and i < len(self.input_string):
            i = i + 1

        # process the sign (if available)
        if self.input_string[i] == self.MINUS_SIGN:
            i = i + 1
        elif self.input_string[i] == self.PLUS_SIGN:
            i = i + 1

        while i < len(self.input_string):
            if self.input_string[i] in string.digits:
                i = i + 1
            elif self.input_string[i] == self.DECIMAL_SIGN:
                i = i + 1
            else:
                return False

        # if we are here, it's a number
        return True
