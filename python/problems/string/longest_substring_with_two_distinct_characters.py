"""
Longest Substring With Two Distinct Characters

Given a string S, find the length of the longest substring T that contains at most two distinct characters.

For example,
Given S = “eceba”,
T is "ece" which its length is 3.
"""
from common.problem import Problem


class LongestSubstringWithTwoDistinctCharacters(Problem):
    """
    Longest Substring With Two Distinct Characters
    """
    PROBLEM_NAME = "LongestSubstringWithTwoDistinctCharacters"

    def __init__(self, input_string):
        """Longest Substring With Two Distinct Characters

        Args:
            input_string: to be checked for longest substring with at least two distinct characters

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_string = input_string
        self.num_distinct = 2

    def solve(self):
        """Solve the problem

        Note: Uses a sliding window template to increment end till (> num_distinct = 2) characters are encountered.
        Then, begin is incremented till the counter for the beginning character becomes 0. max_length is updated based
        on the current begin and end.
        This is an O(n) run time solution with a space complexity of O(n) (due to using a map for storing per character count)

        Args:

        Returns:
            integer

        Raises:
            None

        Reference:
            https://github.com/cherryljr/LeetCode/blob/master/Longest%20Substring%20with%20At%20Most%20Two%20Distinct%20Characters.java
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if len(self.input_string) == 0:
            return 0

        max_length = 0
        count_dict = {}
        begin = 0
        end = 0
        counter = 0

        while end < len(self.input_string):
            # start from the end character
            char_end = self.input_string[end]
            count_dict[char_end] = count_dict.get(char_end, 0) + 1

            # increment new character count if the count is 1
            if count_dict[char_end] == 1:
                counter = counter + 1

            # move end to the next character
            end = end + 1

            # while we have seen > num_distinct characters, decrement counter for the begin
            while counter > self.num_distinct:
                char_begin = self.input_string[begin]
                count_dict[char_begin] = count_dict.get(char_begin) - 1
                if count_dict.get(char_begin) == 0:
                    counter = counter - 1
                begin = begin + 1

            # assign max_length based on the end and begin for each iteration
            max_length = max(max_length, end - begin)

        return max_length
