class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        
        for i in prices:
            min_price = min(i, min_price)
            profit = i - min_price
            max_profit = max(max_profit, profit)
        
        return max_profit