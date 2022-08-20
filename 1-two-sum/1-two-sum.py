class Solution(object):
    def twoSum(self, nums, target):
        
        hashmap = {}
        
        for i in range(len(nums)):
            hashmap[nums[i]] = i
            
        for i in range(len(nums)):
            contemplate = target - nums[i]
            
            if contemplate in hashmap and hashmap[contemplate] != i:
                return [i, hashmap[contemplate]]