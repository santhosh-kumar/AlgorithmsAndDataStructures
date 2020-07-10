"""
Generate All Parantheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""
from common.problem import Problem


class GenerateAllParantheses(Problem):
    """
    GenerateAllParantheses
    """
    PROBLEM_NAME = "GenerateAllParantheses"

    def __init__(self, n):
        """GenerateAllParantheses

        Args:
            n: number of parantheses

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.n = n

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
        current = ""
        open = 0
        close = 0
        max = self.n

        self.generate(result, current, open, close, max)

        return result

    def generate(self, result, current, open, close, max):
        """Generate n valid parantheses

        Args:
            result: collect all the valid solutions
            current: the current partial solution
            open: currently open count
            close: currently closed count
            max: max allowed parantheses

        Returns:

        Raises:
            None
        """
        if len(current) == max * 2:
            result.append(current)
            return

        if open < max:
            self.generate(result, current + "(", open + 1, close, max)

        if close < open:
            self.generate(result, current + ")", open, close + 1, max)
