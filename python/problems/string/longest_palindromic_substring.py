"""
Longest Palindromic Substring

Given a string S, find the longest palindromic substring in S. You may assume that the
maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""
from common.problem import Problem


class LongestPalindromicSubstring(Problem):
    """
    LongestPalindromicSubstring
    """
    PROBLEM_NAME = "LongestPalindromicSubstring"

    def __init__(self, input_string):
        """Longest Palindromic Substring

        Args:
            input_string: input_string to be checked longest palindromic substring

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_string = input_string

    def solve(self):
        """Solve the problem

        Note: The O(n^2)(runtime) and O(1) (space) solution exploits the fact that there are 2n-1 palindromic centers in a given string.
        At each iteration, expand around those palindromic centers (character and between characters).

        For example, a string of size 5 would have 9 palindromic centers (5 characters and 4 between characters).

        Args:

        Returns:
            string

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if self.input_string == "":
            return ""

        start = 0
        end = 0

        for i in range(len(self.input_string)):
            # check on the character
            length1 = self.expand_around_center(self.input_string, i, i)

            # check between characters
            length2 = self.expand_around_center(self.input_string, i, i + 1)

            length = max(length1, length2)

            # adjust the start and the end based on the length of the longest palindrome
            if length > end - start:
                start = int(i - (length - 1) / 2)
                end = int(i + length / 2)

        return self.input_string[start:end + 1]

    @staticmethod
    def expand_around_center(input_string, left_index, right_index):
        """Expand around the center

        Args:
            input_string: Given string
            left_index: expanded to left on matching characters
            right_index: expanded to right on matching characters

        Returns:
            integer

        Raises:
            None
        """
        while left_index >= 0 \
                and right_index < len(input_string) \
                and input_string[left_index] == input_string[right_index]:
            left_index = left_index - 1
            right_index = right_index + 1

        # length of palindromic string
        return right_index - left_index - 1
