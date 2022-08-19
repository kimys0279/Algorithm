class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        if len(nums) == 1:
            return nums
        for i in range(1, len(nums) + 1):
            res.append(sum(nums[:i]))
        return res