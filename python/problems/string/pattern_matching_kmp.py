"""
Pattern Matching (Knuth-Morris-Pratt)

Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[])
that prints all occurrences of pat[] in txt[]. You may assume that n > m.
"""
from common.problem import Problem


class PatternMatchingKMPAlgorithm(Problem):
    """
    Pattern Matching (KMP)
    """
    PROBLEM_NAME = "PatternMatchingKMPAlgorithm"
    NOT_FOUND = -1

    def __init__(self, input_string, pattern):
        """StrStr

        Args:
            input_string: haystack
            pattern: to be searched in the haystack

        Returns:
            list

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_string = input_string
        self.pattern = pattern

    def solve(self):
        """Solve the problem

        Note: O(n) (runtime) solution works by calculating the longest prefix which is also a suffix table.
        Using the LPS array, the index (j) for the pattern is moved back only to the right point while comparison.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        lps_array = self.get_lps_array(self.pattern)
        result = []
        j = 0

        for i in range(len(self.input_string)):
            while j > 0 and self.input_string[i] != self.pattern[j]:
                j = lps_array[j - 1]

            if self.input_string[i] == self.pattern[j]:
                j += 1

            if j == len(self.pattern):
                result.append(i - (j - 1))
                j = lps_array[j - 1]

        return result

    @staticmethod
    def get_lps_array(pattern):
        """Longest Prefix which is also Suffix array

        Args:
            pattern: to derive the lps array for

        Returns:
            integer

        Raises:
            None
        """
        ret = [0]

        # iterate characters in the pattern
        for i in range(1, len(pattern)):
            j = ret[i - 1]

            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]

            ret.append(j + 1 if pattern[j] == pattern[i] else j)

        return ret
