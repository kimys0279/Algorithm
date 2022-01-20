class Solution(object):
   
    def search(self, nums, target):
        if target not in nums:
            return -1
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        