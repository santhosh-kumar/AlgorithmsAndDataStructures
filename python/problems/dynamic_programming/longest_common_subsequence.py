"""
Longest Common Subsequence

Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.
"""
from common.problem import Problem


class LongestCommonSubsequence(Problem):
    """
    LongestCommonSubsequence
    """
    PROBLEM_NAME = "LongestCommonSubsequence"
    NOT_FOUND = -1

    def __init__(self, input_string1, input_string2):
        """LongestCommonSubsequence

        Args:
            input_string1: First string
            input_string2: Second string

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
        Args:

        Note: O(mn) solution uses dynamic programming to find matches.

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        len1 = len(self.input_string1)
        len2 = len(self.input_string2)

        lcs_matrix = [[None] * (len2 + 1) for i in range(len1 + 1)]

        """Following steps build lcs_matrix[m+1][n+1] in bottom up fashion 
        Note: L[i][j] contains length of LCS of string1[0..i-1] 
        and string2[0..j-1]"""

        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == 0 or j == 0:
                    lcs_matrix[i][j] = 0
                elif self.input_string1[i - 1] == self.input_string2[j - 1]:
                    lcs_matrix[i][j] = lcs_matrix[i - 1][j - 1] + 1
                else:
                    lcs_matrix[i][j] = max(lcs_matrix[i - 1][j], lcs_matrix[i][j - 1])

        return lcs_matrix[len1][len2]
