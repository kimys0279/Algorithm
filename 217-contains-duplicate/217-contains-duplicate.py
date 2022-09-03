class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        li = set(nums)
        return len(li) != len(nums)