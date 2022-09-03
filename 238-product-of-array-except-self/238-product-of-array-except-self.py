import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right, result = [1]*n, [1]*n, [1]*n
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
            
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
            
        for i in range(len(nums)):
            result[i] = left[i] * right[i]
            
        return result