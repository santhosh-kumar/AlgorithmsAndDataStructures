"""
Wildcard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".


Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.


Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.


Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".


Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""
from common.problem import Problem


class WildcardMatching(Problem):
    """
    WildcardMatching
    """
    PROBLEM_NAME = "WildcardMatching"

    def __init__(self, input_string, pattern):
        """StrStr

        Args:
            input_string: haystack
            pattern: to be searched in the haystack

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_string = input_string
        self.pattern = pattern

    def solve(self):
        """Solve the problem

        Note: O(mn), space complexity: O(mn), where n = len(s), m = len(p).

        Args:

        Returns:
            boolean

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        input_string_length = len(self.input_string)
        pattern_length = len(self.pattern)

        match_matrix = [[False] * (input_string_length + 1) for _ in range(pattern_length + 1)]
        match_matrix[0][0] = True

        for i in range(1, pattern_length + 1):
            match_matrix[i][0] = match_matrix[i - 1][0] and self.pattern[i - 1] == '*'

        for i in range(1, pattern_length + 1):
            for j in range(1, input_string_length + 1):
                if self.pattern[i - 1] != '*':
                    match_matrix[i][j] = (self.pattern[i - 1] == self.input_string[j - 1] or self.pattern[
                        i - 1] == '?') and match_matrix[i - 1][j - 1]
                else:
                    match_matrix[i][j] = match_matrix[i][j - 1] or match_matrix[i - 1][j]

        return match_matrix[-1][-1]
