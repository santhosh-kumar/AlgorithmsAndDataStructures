"""
0/1 Knapsack

Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.

In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively.
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such
that sum of the weights of this subset is smaller than or equal to W.

You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
"""
from common.problem import Problem


class ZeroOneKnapsack(Problem):
    """
    Zero One Knapsack
    """
    PROBLEM_NAME = "ZeroOneKnapsack"

    def __init__(self, values, weights, capacity):
        """ZeroOneKnapsack

        Args:
            values: Value of the items
            weights: Weights of the items
            capacity: Maximum capacity of the knapsack

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.values = values
        self.weights = weights
        self.capacity = capacity

    def solve(self):
        """Solve the problem

        Note:

        Args:

        Returns:
            tuple

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))

        number_values = len(self.values)

        sack_matrix = [[0 for x in range(self.capacity + 1)] for x in range(number_values + 1)]

        for i in range(number_values + 1):
            for w in range(self.capacity + 1):
                if i == 0 or w == 0:
                    sack_matrix[i][w] = 0
                elif self.weights[i - 1] <= w:
                    # current item's weight is possible.
                    # If so, choose the max last item's possibility or current value + previous possibility with w-current weight
                    sack_matrix[i][w] = max(sack_matrix[i - 1][w],
                                            self.values[i - 1] + sack_matrix[i - 1][w - self.weights[i - 1]])
                else:
                    sack_matrix[i][w] = sack_matrix[i - 1][w]

        return sack_matrix[number_values][self.capacity]
