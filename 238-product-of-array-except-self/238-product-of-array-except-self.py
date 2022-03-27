class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        left, right, result = [1]*n, [1]*n, [1]*n
        for i in range(1, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]  # nums[i-1] 4, 1, 2, 3 // left 1 1 1 1 // left = 1 1 2 6
            
        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i+1] * right[i+1]  #nums[i+1] 2, 3, 4, 1 // right 1 1 1 1 // right = 24 12 4 1 
            
        for i in range(0, len(nums)):
            result[i] = left[i] * right[i]
            
        return result