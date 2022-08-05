class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0 or k > len(s):
            return 0
        
        c = Counter(s)
        sub1, sub2 = "", ""
        
        for i, j in enumerate(s):
            if c[j] < k:
                sub1 = self.longestSubstring(s[:i], k)
                sub2 = self.longestSubstring(s[i+1:], k)
                break
        else:
            return len(s)

        return max(sub1, sub2)