"""
Letter Phone

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
from common.problem import Problem


class LetterPhone(Problem):
    """
    LetterPhone
    """
    PROBLEM_NAME = "LetterPhone"

    MAPPINGS = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def __init__(self, input_integer):
        """LetterPhone

        Args:
            input_integer: Integer

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_integer = input_integer

    def solve(self):
        """Solve the problem

        Note:

        Args:

        Returns:
            list(list)

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        result = []
        digits = list(str(self.input_integer))

        return self.combine(result, digits)

    def combine(self, result, remaining_digits):
        """Combine

        Args:
            result: collect all the valid solutions
            remaining_digits: remaining digits

        Returns:

        Raises:
            None
        """
        if len(remaining_digits) == 0:
            return result

        if len(result) == 0:
            result = ['']

        next_result = []

        digit = remaining_digits.pop(0)
        for r in result:
            for c in self.MAPPINGS[digit]:
                next_result.append(r + c)
        return self.combine(next_result, remaining_digits)  # nxt_rst = r+c
