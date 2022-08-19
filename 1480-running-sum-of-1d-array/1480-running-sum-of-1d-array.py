class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(1, len(nums) + 1):
            res.append(sum(nums[:i]))
        return res