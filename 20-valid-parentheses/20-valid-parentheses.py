class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':1, ')':2, '{':3, '}':4, '[':5, ']':6}
        ans = []
        
        for bra in s:
            if dic[bra] % 2 == 1:
                ans.append(dic[bra])
            else:
                if len(ans) != 0 and ans[-1] == dic[bra] - 1:
                    ans.pop()
                else:
                    return False 
        return len(ans) == 0