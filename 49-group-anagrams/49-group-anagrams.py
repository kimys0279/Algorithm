class Solution(object):
    def groupAnagrams(self, strs):
        ans = []
        strdic = {}
        
        for i in strs:
            a = ''.join(sorted(i))
            print(a)
            
            if a in strdic:
                strdic[a].append(i)
            else:
                strdic[a] = [i]
                
        for key, val in strdic.items():
            ans.append(val)
            
        print(ans)
        return ans