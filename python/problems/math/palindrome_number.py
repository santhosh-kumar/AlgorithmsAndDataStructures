"""
Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

Example Questions Candidate Might Ask:

Q: Does negative integer such as –1 qualify as a palindrome?
A: For the purpose of discussion here, we define negative integers as non-palindrome.

"""
from common.problem import Problem


class PalindromeNumber(Problem):
    """
    PalindromeNumber
    """
    PROBLEM_NAME = "PalindromeNumber"

    def __init__(self, input_integer):
        """Palindrome Number

        Args:
            input_integer: to be checked if it's a palindrome

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

        Note: O(n) solution works by comparing left and right most digits until they are different or all the numbers are seen.

        Args:

        Returns:
            boolean

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if self.input_integer < 0:
            return False

        input_integer = self.input_integer

        # find the max divisor for the given input_integer (1000000 for 1234321)
        divisor = 1
        while int(input_integer / divisor) > 10:
            divisor = divisor * 10

        while input_integer != 0:
            # get the left most digit
            left_digit = int(input_integer / divisor)

            # get the right most digit
            right_digit = input_integer % 10

            if left_digit != right_digit:
                return False

            # omit right and left most digits
            input_integer = int((input_integer % divisor) / 10)

            # adjust the divisor according to the current input_integer (ignore 2 zeroes)
            divisor = divisor / 100

        return True
