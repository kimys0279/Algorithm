class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        total_sum = 0
        cache = {}
        for i in nums3:
            for j in nums4:
                key = i + j
                if key in cache:
                    cache[key] += 1
                else:
                    cache[key] = 1
        for i in nums1:
            for j in nums2:
                key = -i-j
                if key in cache:
                    total_sum += cache[key]
                    
        return total_sum