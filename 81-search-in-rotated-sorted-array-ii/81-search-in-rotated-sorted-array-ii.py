class Solution(object):
    def search(self, nums, target):
        if not nums:
            return False
        if target not in nums:
            return False
        return True
        
        
    
    def search1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if target in nums:
            return True
        return False
    
    def search2(self, nums, target):
        if not nums:
            return False
        
        l, h = 0, len(nums) - 1
        
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return True
            
            while l < mid and nums[l] == nums[mid]:
                l += 1
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            
            else:
                if nums[mid] < target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        return False