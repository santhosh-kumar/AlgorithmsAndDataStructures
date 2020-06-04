"""
Plus One

Given a number represented as an array of digits, plus one to the number.

Example Questions Candidate Might Ask:

Q: Could the number be negative?
A: No. Assume it is a non-negative number.

Q: How are the digits ordered in the list? For example, is the number 12 represented by [1,2] or
[2,1]?
A: The digits are stored such that the most significant digit is at the head of the list.

Q: Could the number contain leading zeros, such as [0,0,1]?
A: No.
"""
from common.problem import Problem


class PlusOne(Problem):
    """
    PlusOne
    """
    PROBLEM_NAME = "PlusOne"

    def __init__(self, input_integers_list):
        """Plus One

        Args:
            input_integers_list: list to which the number to be added
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_integers_list = input_integers_list

    def solve(self):
        """Solve the problem
           Note:
        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        overflow = 1
        for i in list(reversed(range(len(self.input_integers_list)))):
            digit = self.input_integers_list[i]
            sum_value = digit + overflow
            if sum_value > 9:
                self.input_integers_list[i] = int(sum_value) % 10
                overflow = 1
            else:
                overflow = 0

            if i == 0 and overflow == 1:
                self.input_integers_list.insert(0, overflow)

        return self.input_integers_list
