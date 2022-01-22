class Solution(object):
    def isAnagram(self, s, t):
        slist = []
        tlist = []
        
        if len(s) != len(t): return False
        
        for i in range(len(s)):
            slist.append(s[i])
            
        for j in range(len(t)):
            tlist.append(t[j])
        
        for com in slist:
            if com not in tlist:
                return False
            else:
                tlist.remove(com)
                
        return True
            