class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        
        for i, val in enumerate(s):
            dic1[val] = dic1.get(val, []) + [i]
            
        for i, val in enumerate(t):
            dic2[val] = dic2.get(val, []) + [i]
            
        return sorted(dic1.values()) == sorted(dic2.values())