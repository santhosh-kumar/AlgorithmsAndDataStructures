"""
Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Example Questions Candidate Might Ask:
Q: What about an empty string? Is it a valid palindrome?
A: For the purpose of this problem, we define empty string as valid palindrome.
"""
import string

from common.problem import Problem


class ValidPalindrome(Problem):
    """
    ValidPalindrome
    """
    PROBLEM_NAME = "ValidPalindrome"

    def __init__(self, input_string):
        """Valid Palindrome

        Args:
            input_string: input_string to be checked if it's a palindrome
        Returns:
            None

        Raises:
            None
        """
        assert (len(input_string) > 0)

        super().__init__(self.PROBLEM_NAME)
        self.input_string = input_string

    def solve(self):
        """Solve the problem

        Note: O(n) works by iterating from left and right sides of the string while skipping empty spaces.
        The solution takes only O(1) space -- no extra array needed.

        Args:

        Returns:
            None

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if self.input_string == "":
            return True

        left_index = 0
        right_index = len(self.input_string) - 1

        while left_index < right_index:
            while not self.is_letter_or_digit(self.input_string[left_index].lower()):
                left_index = left_index + 1

            while not self.is_letter_or_digit(self.input_string[right_index].lower()):
                right_index = right_index - 1

            if self.input_string[left_index].lower() != self.input_string[right_index].lower():
                return False

            left_index = left_index + 1
            right_index = right_index - 1

        # If we are here, both left and right indices met and we have a palindrome
        return True

    @staticmethod
    def is_letter_or_digit(input_character):
        """Checks if the given character is a letter or a digit

        Args:
            input_character: to be checked

        Returns:
            Boolean (True|False)

        Raises:
            None
        """
        if input_character not in string.digits and input_character not in string.ascii_lowercase:
            return False

        return True
