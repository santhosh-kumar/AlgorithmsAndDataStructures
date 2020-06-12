"""
Reverse Words in a string (in place)

Question:
Given an input string s, reverse the string word by word.
For example, given s = "the sky is blue", return "blue is sky the".

Constraint:
“The input string does not contain leading or trailing spaces and the words are always
separated by a single space.”

Could you do it in-place without allocating extra space?
"""
from common.problem import Problem


class ReverseStringWordsInPlace(Problem):
    """
    TwoSum
    """
    PROBLEM_NAME = "ReverseStringWordsInPlace"
    BYTE_SPACE = 32

    def __init__(self, input_string):
        """Reverse String Words (in place)

        Args:
            input_string: to be reversed by words

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

        Note: O(n) (runtime) and O(1) (space-constraint) works by reversing the string first. Then, iterates the byte array until a space (32) is reached.
        When a space is reached, the word between spaces is reversed.

        Args:

        Returns:
            string

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        self.input_string = self.reverse(self.input_string)
        self.input_string = bytearray(self.input_string, 'ascii')

        last_space_index = -1
        i = 0
        while i < len(self.input_string):
            if self.input_string[i] == self.BYTE_SPACE:
                self.input_string[last_space_index + 1: i] = self.reverse(self.input_string[last_space_index + 1:i])
                last_space_index = i
            i = i + 1

        # we have reached the end, reverse the last processed word
        self.input_string[last_space_index + 1: i] = self.reverse(self.input_string[last_space_index + 1:i])

        return self.input_string.decode('ascii')

    @staticmethod
    def reverse(value):
        return value[::-1]
