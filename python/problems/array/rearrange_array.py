"""
Rearrange Array

Given an array arr[] of size n where every element is in range from 0 to n-1.
Rearrange the given array so that arr[i] becomes arr[arr[i]]. This should be done with O(1) extra space.

Input: arr[]  = {3, 2, 0, 1}
Output: arr[] = {1, 0, 3, 2}

Explanation:

In the given array
arr[arr[0]] is 1 so arr[0] in output array is 1
arr[arr[1]] is 0 so arr[1] in output array is 0
arr[arr[2]] is 3 so arr[2] in output array is 3
arr[arr[3]] is 2 so arr[3] in output array is 2
"""
from common.problem import Problem


class RearrangeArray(Problem):
    """
    Rearrange Array
    """
    PROBLEM_NAME = "RearrangeArray"

    def __init__(self, input_list):
        """Rearrange Array

        Args:
            input_list: Contains a list of integers

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list

    def solve(self):
        """Solve the problem

        Note: O(n) (runtime) and O(1) (space) works by first increasing the values of the array and then dividing by n.
        Let’s assume an element is a and another element is b, both the elements are less than n. So if an element a is
        incremented by b*n. So the element becomes a + b*n so when a + b*n is divided by n then the value
        is b and a + b*n % n is a.

        Args:

        Returns:
            list

        Raises:
            None
        """
        n = len(self.input_list)

        # First step: Increase all values by (arr[arr[i]] % n) * n
        for i in range(0, n):
            self.input_list[i] = self.input_list[i] + ((self.input_list[self.input_list[i]] % n) * n)

        # Second Step: Divide all values by n
        for i in range(0, n):
            self.input_list[i] = int(self.input_list[i] / n)

        return self.input_list
