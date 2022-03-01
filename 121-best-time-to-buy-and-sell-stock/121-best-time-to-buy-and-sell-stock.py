class Solution(object):

    def maxProfit1(self, prices):
        if len(prices) == 0:
            return 0
        
        max = prices[-1]
        profit = 0
        
        for item in prices[::-1]:
            if max - item > profit:
                profit = max - item
            if item > max:
                max = item
        return profit
    
    
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        
        sell = prices[-1]
        profit = 0
        
        for buy in prices[::-1]:
            if sell - buy > profit:
                profit = sell - buy
            if sell < buy:
                sell = buy
        return profit