"""
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for “abcabcbb” is “abc”, which
the length is 3. For “bbbbb” the longest substring is “b”, with the length of 1.
"""
from common.problem import Problem


class LongestSubstringWithoutRepeatingCharacters(Problem):
    """
    LongestSubstringWithoutRepeatingCharacters
    """
    PROBLEM_NAME = "LongestSubstringWithoutRepeatingCharacters"

    def __init__(self, input_string):
        """Longest Substring Without Repeating Characters

        Args:
            input_string: to be checked for longest substring without repeating characters

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_string = input_string

    def solve(self):
        """Solve the problem

        Note: O(n) (runtime) and O(1) (space) iterates over the string, checks if the character is seen so far.
        If not, increment the string count.
        Search operations in list and dict take O(1).

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if len(self.input_string) == 0:
            return 0

        i = 0
        max_length = 0
        current_length = 0
        input_string_list = [char for char in self.input_string]

        while i < len(input_string_list):
            if input_string_list[i] not in input_string_list[0:i]:
                current_length = current_length + 1
            else:
                if current_length > max_length:
                    max_length = current_length
                    current_length = 1
            i = i + 1

        return max_length
