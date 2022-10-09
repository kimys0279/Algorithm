class Solution:
    def climbStairs(self, n: int) -> int:
        nums = [1, 2]
        
        for i in range(2, n+1):
            nums.append(nums[i-1]+nums[i-2])
            
        return nums[n-1]