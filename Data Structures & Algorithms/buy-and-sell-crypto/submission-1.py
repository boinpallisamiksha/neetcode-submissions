class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                current = prices[j] - prices[i]
                if current > max_profit:
                    max_profit = current
        return max_profit
