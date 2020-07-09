"""
Add two binary strings

Given two binary strings, return their sum (also a binary string).

Example:

a = "100"

b = "11"

Return a + b = “111”.
"""
from common.problem import Problem


class AddTwoBinaryStrings(Problem):
    """
    AddTwoBinaryStrings
    """
    PROBLEM_NAME = "AddTwoBinaryStrings"
    NOT_FOUND = -1

    def __init__(self, input_string1, input_string2):
        """AddTwoBinaryStrings

        Args:
            input_string1: First binary string
            input_string1: Second binary string

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_string1 = input_string1
        self.input_string2 = input_string2

    def solve(self):
        """Solve the problem

        Note:

        Args:

        Returns:
            string

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        max_len = max(len(self.input_string1), len(self.input_string2))

        self.input_string1.zfill(max_len)
        self.input_string2.zfill(max_len)

        carry = 0
        result = ''
        for i in range(max_len - 1, -1, -1):
            char1 = self.input_string1[i]
            char2 = self.input_string2[i]

            r = carry
            if char1 == '1':
                r = r + 1

            if char2 == '1':
                r = r + 1

            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1

        if carry != 0:
            result = '1' + result

        return result.zfill(max_len)
