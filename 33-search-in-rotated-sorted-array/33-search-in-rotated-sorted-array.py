class Solution(object):
   
    def search(self, nums, target):
        if target not in nums:
            return -1
        
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) / 2
            
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1