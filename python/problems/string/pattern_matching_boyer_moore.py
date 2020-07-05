"""
Pattern Matching (Boyer Moore)

Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[])
that prints all occurrences of pat[] in txt[]. You may assume that n > m.
"""
from common.problem import Problem


class PatternMatchingBoyerMooreAlgorithm(Problem):
    """
    Pattern Matching (Boyer Moore)
    """
    PROBLEM_NAME = "PatternMatchingBoyerMooreAlgorithm"
    NOT_FOUND = -1
    NUMBER_CHARACTERS = 256

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

        Note: The average runtime is O(n). The Bad Character Heuristic may take O(mn) time in worst case.
        The worst case occurs when all characters of the text and pattern are same.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        bad_match_table = self.get_bad_match_table(self.pattern)

        i = 0
        s = i + len(self.pattern) - 1

        while s < len(self.input_string):
            j = s
            p = len(self.pattern) - 1  # index for pattern

            # following compares the pattern from right with the given substring starting at j and ending at ith location (j > i)
            while j >= i:
                if self.input_string[j] != self.pattern[p]:
                    # calculate good shift from the bad character table
                    s = s + self.get_good_shift(bad_match_table, self.input_string[j])
                    i = s - len(self.pattern) + 1
                    break
                else:
                    # we have matched the pattern with the sub-string
                    if j == i:
                        return i + 1
                    # characters matched so far
                    j = j - 1
                    p = p - 1

        return self.NOT_FOUND

    @staticmethod
    def get_bad_match_table(pattern):
        """Get bad match table for the pattern

        Args:
            pattern: pattern for which to construct the bad match table

        Returns:
            list

        Raises:
            None
        """
        bad_match_table = {}
        pattern_length = len(pattern)
        for i in range(pattern_length):
            ch = pattern[i]
            bad_match_table[ch] = pattern_length - i - 1

        return bad_match_table

    def get_good_shift(self, bad_match_table, mismatch_character):
        """Return the good shift position

        Args:
            bad_match_table: bad_match_table
            mismatch_character: character that was mismatched

        Returns:
            integer

        Raises:
            None
        """
        return bad_match_table.get(mismatch_character, len(self.pattern))
