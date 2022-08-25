class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        shortest = min(strs, key = len)
        for i, c in enumerate(shortest):
            for others in strs:
                if others[i] != c:
                    return shortest[:i]
        return shortest