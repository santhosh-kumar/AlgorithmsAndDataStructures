"""
Pattern Matching (Rabin Karp)

Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[])
that prints all occurrences of pat[] in txt[]. You may assume that n > m.
"""
from common.problem import Problem


class PatternMatchingRabinKarpAlgorithm(Problem):
    """
    Pattern Matching (Rabin Karp)
    """
    PROBLEM_NAME = "PatternMatchingRabinKarpAlgorithm"
    NOT_FOUND = -1

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

        Note: The average and best case running time is O(n+m) and the worst case is O(nm).

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        pattern_length = len(self.pattern)
        pattern_hash = self.bernstein_hash(self.pattern)

        for i in range(len(self.input_string) - pattern_length):
            if self.bernstein_hash(self.input_string[i:i + pattern_length]) == pattern_hash:
                return i + 1

        return self.NOT_FOUND

    @staticmethod
    def bernstein_hash(value):
        """Bernstein hash value of the string

        Note:

        Args:
            value: string to hash

        Returns:
            integer

        Raises:
            None
        """
        value_bytes = bytearray(value, 'ascii')
        hash_value = 5381
        for c in value_bytes:
            hash_value = hash_value * 33 + c

        return hash_value
