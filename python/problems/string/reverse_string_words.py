"""
Reverse Words in a string

Question:
Given an input string s, reverse the string word by word.
For example, given s = "the sky is blue", return "blue is sky the".

Example Questions Candidate Might Ask:
Q: What constitutes a word?
A: A sequence of non-space characters constitutes a word.

Q: Does tab or newline character count as space characters?
A: Assume the input does not contain any tabs or newline characters.

Q: Could the input string contain leading or trailing spaces?
A: Yes. However, your reversed string should not contain leading or trailing spaces.

Q: How about multiple spaces between two words?
A: Reduce them to a single space in the reversed string.
"""
from common.problem import Problem


class ReverseStringWords(Problem):
    """
    TwoSum
    """
    PROBLEM_NAME = "ReverseStringWords"

    def __init__(self, input_string):
        """Reverse String Words

        Note: Brute force solution would be to do two passes over the string to first to split strings by space and put into a list.
        In the seconds pass, iterate the list in the reverse order.

        For an one-pass solution, iterate string in reverse order until a space is hit. Then, use the word the seen thus far as the chosen word.
        It takes O(n) runtime and O(n) space.

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
        Args:

        Returns:
            string

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if self.input_string == "":
            return ""

        reversed_string = ""
        word = ""
        for i in list(reversed(range(len(self.input_string)))):
            is_space_found = False
            if self.input_string[i] != " ":
                word = self.input_string[i] + word
            else:
                is_space_found = True

            if is_space_found or i == 0:
                if reversed_string != "":
                    reversed_string = reversed_string + " " + word
                else:
                    reversed_string = word
                word = ""

        return reversed_string
