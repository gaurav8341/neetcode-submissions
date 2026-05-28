class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_stock = prices[0]
        profit = 0#int("-infinity")

        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - min_stock)
            min_stock = min(min_stock, prices[i])
        
        return profit