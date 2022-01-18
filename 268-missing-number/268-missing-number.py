class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        big = len(nums)

        orisum = ((big + 1) * big) / 2

        return orisum - sum(nums)
