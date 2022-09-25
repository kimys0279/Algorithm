class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        if n == 0:
            return 0
        prod = 1
        sums = 0
        for i in str(n):
            prod *= int(i)
            
        for i in str(n):
            sums += int(i)
        
        return prod - sums