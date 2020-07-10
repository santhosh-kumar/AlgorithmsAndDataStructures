"""
Four Equal

Given an array of distinct integers, find if there are two pairs (a, b) and (c, d) such that a+b = c+d, and a, b, c and d are distinct elements.
If there are multiple answers, then print any of them.

Example:

Input:   {3, 4, 7, 1, 2, 9, 8}
Output:  (3, 8) and (4, 7)
Explanation: 3+8 = 4+7

Input:   {3, 4, 7, 1, 12, 9};
Output:  (4, 12) and (7, 9)
Explanation: 4+12 = 7+9

Input:  {65, 30, 7, 90, 1, 9, 8};
Output:  No pairs found

Expected Time Complexity: O(n^2)
"""
from common.problem import Problem


class FourEqual(Problem):
    """
    Equal
    """
    PROBLEM_NAME = "FourEqual"

    def __init__(self, input_list):
        """FourEqual

        Args:
            input_list: Contains a list of integers

        Returns:
            None

        Raises:
            None
        """
        assert (len(input_list) > 0)

        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list

    def solve(self):
        """Solve the problem

        Note:

        Args:

        Returns:
            list

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        sum_dict = {}
        n = len(self.input_list)

        result = []

        for i in range(n - 1):
            for j in range(i + 1, n):
                total = self.input_list[i] + self.input_list[j]
                candidate = [self.input_list[i], self.input_list[j]]
                if total in sum_dict.keys():
                    result.append(sum_dict[total] + candidate)
                else:
                    sum_dict[total] = candidate

        return result
