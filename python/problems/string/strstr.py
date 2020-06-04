"""
StrStr

Implement strstr(). Returns the index of the first occurrence of needle in haystack, or –1 if needle is not part of haystack.

Have you considered these scenarios?
i. needle or haystack is empty. If needle is empty, always return 0. If haystack is
empty, then there will always be no match (return –1) unless needle is also empty which 0 is returned.

ii. needle’s length is greater than haystack’s length. Should always return –1.

iii. needle is located at the end of haystack. For example, “aaaba” and “ba”. Catch possible off-by-one errors.

iv. needle occur multiple times in haystack. For example, “mississippi” and “issi”. It should return index 2 as the first match of “issi”.

v. Imagine two very long strings of equal lengths = n, haystack = “aaa…aa” and
needle = “aaa…ab”. You should not do more than n character comparisons, or else your code will get Time Limit Exceeded in OJ.
"""
from common.problem import Problem


class StrStr(Problem):
    """
    StrStr
    """
    PROBLEM_NAME = "StrStr"
    NOT_FOUND = -1

    def __init__(self, input_string, needle):
        """StrStr

        Args:
            input_string: haystack
            needle: to be searched in the haystack
        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_string = input_string
        self.needle = needle

    def solve(self):
        """Solve the problem
        Args:
        Note: O(nm) runtime solution works by iterating the input_string character by character (n) and comparing with the m characters in the needle.
        It requires a constant space i.e., O(1)

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if len(self.input_string) == 0 or len(self.needle) == 0:
            return 0

        if len(self.needle) > len(self.input_string):
            return self.NOT_FOUND

        input_len = len(self.input_string)
        needle_len = len(self.needle)

        for i in range(input_len):
            input_string_index = i
            needle_index = 0

            while needle_index < needle_len \
                    and input_string_index < input_len \
                    and self.input_string[input_string_index] == self.needle[needle_index]:
                input_string_index = input_string_index + 1
                needle_index = needle_index + 1

            if needle_index == needle_len:
                return i + 1

        # if we are here, we haven't found the match
        return self.NOT_FOUND
