"""
Max Product SubArray

Find the contiguous subarray within an array of integers that has the largest product.

For example, given the array [2,3,-2,4], the contiguous subarray [2,3] has the largest product = 6.
"""
from common.problem import Problem


class MaxProductSubArray(Problem):
    """
    Max Product SubArray
    """
    PROBLEM_NAME = "MaxProductSubArray"

    def __init__(self, input_list):
        """Max Product SubArray

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

        Note: O(n) (runtime) and O(1) (space) solution uses dynamic programming to compute max product and min product at every element.
        min product is calculated for taking negative numbers into account i.e., -2 x -4 = 8.

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        if len(self.input_list) == 0:
            return 0

        max_value = self.input_list[0]
        min_value = self.input_list[0]
        max_product = self.input_list[0]

        for i in range(1, len(self.input_list)):
            mx = max_value
            mn = min_value

            max_value = max(max(mx * self.input_list[i], self.input_list[i]), mn * self.input_list[i])

            min_value = min(min(mx * self.input_list[i], self.input_list[i]), mn * self.input_list[i])

            max_product = max(max_value, max_product)

        return max_product
