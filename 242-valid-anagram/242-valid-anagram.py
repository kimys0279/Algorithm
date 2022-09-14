class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dic_s = {}
        dic_t = {}
        
        for i in s:
            if i not in dic_s:
                dic_s[i] = 1
            dic_s[i] += 1
        
        for i in t:
            if i not in dic_t:
                dic_t[i] = 1
            dic_t[i] += 1
        
        return dic_s == dic_t