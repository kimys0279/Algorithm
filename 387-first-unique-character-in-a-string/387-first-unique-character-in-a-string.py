class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        for i in hashmap:
            if hashmap[i] == 1:
                return s.index(i)
        
        return -1