class Solution(object):
    def maxProfit(self, prices):

        if len(prices) == 0:
            return 0
        
        max = prices[-1]
        profit = 0
        
        for item in prices[::-1]:
            if max - item > profit:
                profit = max - item
            elif item > max:
                max = item
        
        return profit