class Solution:
    def climbStairs(self, n: int) -> int:
        li = [2, 3]
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        for i in range(2, n - 1):
            li.append(li[i-2] + li[i-1])
        
        return li.pop()