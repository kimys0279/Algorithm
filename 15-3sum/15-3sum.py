class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            mid, right = i + 1, len(nums) - 1
            
            while mid < right:
                s = nums[i] + nums[mid] + nums[right]
                if s < 0:
                    mid += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[mid], nums[right]])
                    
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1
                    mid += 1
                    right -= 1
        return res
    
