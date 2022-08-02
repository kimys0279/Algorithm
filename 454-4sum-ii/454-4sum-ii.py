class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hashtable = {}
        for a in nums1:
            for b in nums2:
                if a+b in hashtable:
                    hashtable[a+b] += 1
                else:
                    hashtable[a+b] = 1
        
        count = 0
        for c in nums3:
            for d in nums4:
                if -c-d in hashtable:
                    count += hashtable[-c-d]
        
        return count