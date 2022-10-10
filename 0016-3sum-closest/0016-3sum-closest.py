class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        
        for i in range(len(nums)):
            l, h = i+1, len(nums) - 1
            while l < h:
                sums = nums[i] + nums[l] + nums[h]
                
                if abs(target - sums) < abs(diff):
                    diff = target - sums
                if sums < target:
                    l += 1
                else:
                    h -= 1
            
            if diff == 0:
                break
        
        return target - diff