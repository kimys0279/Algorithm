class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        used = {}
        
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            
            used[c] = i
        
        return maxLength