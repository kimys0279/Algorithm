class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            if target > nums[-1]:
                return nums.index(nums[-1]) + 1
            for i in nums:
                if i > target:
                    return nums.index(i)
        return nums.index(target)