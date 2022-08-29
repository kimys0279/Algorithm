class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        new = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[new]:
                new += 1
                nums[new] = nums[i]
        
        return new + 1