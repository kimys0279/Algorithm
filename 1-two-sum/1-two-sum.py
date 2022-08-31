class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        for i in range(len(nums)):
            contemplate = target - nums[i]
            
            if contemplate in hashmap and hashmap[contemplate] != i:
                return [i, hashmap[contemplate]]