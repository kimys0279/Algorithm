class Solution(object):
    def search(self, nums, target):
        if not nums or target not in nums:
            return -1
        return nums.index(target)
    
    def search1(self, nums, target):
        if not nums or target not in nums:
            return -1
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) //2
            
            if nums[m] == target:
                return m
            
            elif nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    