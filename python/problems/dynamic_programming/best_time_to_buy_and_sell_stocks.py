"""
Best Time to Buy and Sell Stocks

Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Return the maximum possible profit.


Input Format
The first and the only argument is an array of integers, A.

Output Format
Return an integer, representing the maximum possible profit.

Example Input
Input 1:
 A = [1, 2]

Input 2:
 A = [1, 4, 5, 2, 4]

Example Output
Output 1:
 1

Output 2:
 4

"""
from common.problem import Problem


class BestTimeToBuyAndSellStocks(Problem):
    """
    BestTimeToBuyAndSellStocks
    """
    PROBLEM_NAME = "BestTimeToBuyAndSellStocks"

    def __init__(self, input_list):
        """Best Time To Buy And Sell Stocks

        Args:
            input_list: input list of integers

        Returns:
            None

        Raises:
            None
        """
        super().__init__(self.PROBLEM_NAME)
        self.input_list = input_list

    def solve(self):
        """Solve the problem

        Note: O(k * n^2) (runtime)

        Args:

        Returns:
            integer

        Raises:
            None
        """
        print("Solving {} problem ...".format(self.PROBLEM_NAME))
        k = 1  # number of transactions
        return self.max_profit(k)

    def max_profit(self, k):
        """Compute max profit

        Args:
            k: number of transactions

        Returns:
            integer

        Raises:
            None
        """
        n = len(self.input_list)

        profit = [[0 for i in range(k + 1)]
                  for j in range(n)]

        for i in range(1, n):
            for j in range(1, k + 1):
                max_so_far = 0

                for l in range(i):
                    max_so_far = max(max_so_far, self.input_list[i] -
                                     self.input_list[l] + profit[l][j - 1])

                profit[i][j] = max(profit[i - 1][j], max_so_far)

        return profit[n - 1][k]
