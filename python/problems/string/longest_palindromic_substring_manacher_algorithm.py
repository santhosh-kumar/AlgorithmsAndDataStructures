"""
Longest Palindromic Substring (Manacher's Algorithm)

Given a string S, find the longest palindromic substring in S. You may assume that the
maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""
from common.problem import Problem


class LongestPalindromicSubstringManacherAlgorithm(Problem):
    """
    LongestPalindromicSubstringManacherAlgorithm
    """
    PROBLEM_NAME = "LongestPalindromicSubstringManacherAlgorithm"

    def __init__(self, input_string):
        """Longest Palindromic Substring (Manacher's Algorithm)

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

        Note: O(n) (runtime)

        Args:

        Returns:
            string

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if self.input_string == "":
            return ""

        # To deal with even length palindromes, transform the input string to 2N+3
        transformed_string = '#'.join('^{}$'.format(self.input_string))
        n = len(transformed_string)

        palindrome_length_list = [0] * n
        center = 0
        right = 0

        for i in range(1, n - 1):
            if right > i:
                middle = 2 * center - i
                palindrome_length_list[i] = min(right - i, palindrome_length_list[middle])

            # Attempt to expand palindrome centered at i
            while transformed_string[i + 1 + palindrome_length_list[i]] == transformed_string[
                i - 1 - palindrome_length_list[i]]:
                palindrome_length_list[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + palindrome_length_list[i] > right:
                center, right = i, i + palindrome_length_list[i]

        # Find the maximum element in P.
        max_len, center_index = max((n, -i) for i, n in enumerate(palindrome_length_list))
        return self.input_string[(-center_index - max_len) // 2: (-center_index + max_len) // 2]
