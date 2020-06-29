"""
Decode Digit Sequence

Let 1 represent ‘A’, 2 represents ‘B’, etc. Given a digit sequence, count the number of possible decodings of the given digit sequence.

Examples:

Input:  digits[] = "121"
Output: 3
// The possible decodings are "ABA", "AU", "LA"

Input: digits[] = "1234"
Output: 3
// The possible decodings are "ABCD", "LCD", "AWD"

An empty digit sequence is considered to have one decoding.
It may be assumed that the input contains valid digits from 0 to 9 and there are no leading 0’s, no extra trailing 0’s and no two or more consecutive 0’s.
"""

from common.problem import Problem


class DecodeDigitSequence(Problem):
    """
    DecodeDigitSequence
    """
    PROBLEM_NAME = "DecodeDigitSequence"

    def __init__(self, input_string):
        """DecodeDigitSequence

        Args:
            input_string: contains the input string

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_string = input_string

    def solve(self):
        """Solve the problem
        Note: O(n) (runtime) and it requires O(n) auxiliary space.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        count = [0] * (len(self.input_string)+1)

        count[0] = 1
        count[1] = 1

        for i in range(2, len(self.input_string)+1):
            count[i] = 0

            # If the last digit is not 0, then last
            # digit must add to the number of words
            if self.input_string[i - 1] > '0':
                count[i] = count[i - 1]

            # If second last digit is smaller than 2
            # and last digit is smaller than 7, then
            # last two digits form a valid character
            if (self.input_string[i - 2] == '1' or
                    (self.input_string[i - 2] == '2' and
                     self.input_string[i - 1] < '7')):
                count[i] += count[i - 2]

        return count[len(self.input_string)]
