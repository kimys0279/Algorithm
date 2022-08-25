class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # res = ""
        
        shortest = min(strs, key = len)
        
        for i, c in enumerate(shortest):
            for other in strs:
                if other[i] != c:
                    return shortest[:i]
        
        return shortest