class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        best_profit = 0
        for index, value in enumerate(prices):
            for n_value in prices[index:]:
                profit = n_value - value
                if profit > best_profit:
                    best_profit = profit

        return best_profit
