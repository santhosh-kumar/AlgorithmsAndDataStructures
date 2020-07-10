"""
Unit Test for best_time_to_buy_and_sell_stocks
"""
from unittest import TestCase

from problems.dynamic_programming.best_time_to_buy_and_sell_stocks import BestTimeToBuyAndSellStocks


class TestBestTimeToBuyAndSellStocks(TestCase):
    """
    Unit test for BestTimeToBuyAndSellStocks
    """

    def test_solve(self):
        """Test solve

        Args:
            self: TestBestTimeToBuyAndSellStocks

        Returns:
            None

        Raises:
            None
        """
        # Given
        input_list = [1, 4, 5, 2, 4]
        stock_problem = BestTimeToBuyAndSellStocks(input_list)

        # When
        result = stock_problem.solve()

        # Then
        self.assertEqual(result, 4)
