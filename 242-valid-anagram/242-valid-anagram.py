class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in s:
            if i not in t:
                return False
            t = t[:t.index(i)] + t[t.index(i)+1:]
        return True