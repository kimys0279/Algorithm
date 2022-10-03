class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        numneg = 0
        
        for i in nums:
            if i < 0:
                numneg += 1
        if numneg % 2 == 1:
            return -1
        return 1