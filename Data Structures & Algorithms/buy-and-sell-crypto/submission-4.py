class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = len(prices) - 2
        buy = prices[len(prices) - 1]
        sell = prices[len(prices) - 1]
        max_profit = 0
        while i >= 0:
            profit = sell - buy
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] > sell:
                if profit > max_profit:
                    max_profit = profit
                sell = prices[i]
                buy = prices[i] 
            i -= 1

        max_profit = max(max_profit, sell - buy)
        return max_profit
