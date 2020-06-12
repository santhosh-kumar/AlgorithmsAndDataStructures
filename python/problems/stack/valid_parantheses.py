"""
Valid Parantheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Example Questions Candidate Might Ask:
Q: Is the empty string valid?
A: Yes.
"""
from common.problem import Problem
from common.stack import Stack


class ValidParantheses(Problem):
    """
    ValidParantheses
    """
    PROBLEM_NAME = "ValidParantheses"
    PARANTHESES_MAP = {"{": "}", "(": ")", "[": "]"}

    def __init__(self, input_string):
        """Valid Parantheses

        Args:
            input_string: input_string to be checked if it's a valid parantheses

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_string = input_string

    def solve(self):
        """Solve the problem

        Note:

        Args:

        Returns:
            boolean

        Raises:
            None
        """
        parantheses_stack = Stack()

        for c in self.input_string:
            if c in self.PARANTHESES_MAP:
                parantheses_stack.push(c)
            elif len(parantheses_stack) == 0 or self.PARANTHESES_MAP[parantheses_stack.pop()] != c:
                return False

        return len(parantheses_stack) == 0
