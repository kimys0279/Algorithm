class Solution(object):
    
    def isValid(self, s):
        stack = []
        dic = {"}":"{", ")":"(", "]":"["}
        
        for bra in s:
            if bra in dic.values():
                stack.append(bra)
            elif bra in dic.keys():
                if stack == [] or dic[bra] != stack.pop():
                    return False
            else:
                return False
        
        return len(stack) == 0
    
    
    def isValid1(self, s):
        
        stack = []
        dic = {")":"(", "}":"{", "]":"["}
        
        for bra in s:
            if bra in dic.values():
                stack.append(bra)
            elif bra in dic.keys():
                if stack == [] or dic[bra] != stack.pop():
                    return False
            else:
                return False
            
        return len(stack) == 0
    
    
    def isValid2(self, s):
        
        dic = {'(':1, ')':2, '{':3, '}':4, '[':5, ']':6}
        ans = []
        
        for one in s:
            if (dic[one] % 2 == 1):
                ans.append(dic[one])
            else:
                if(len(ans) and ans[-1] == dic[one] - 1):
                    del ans[-1]
                else:
                    return False
                
        return ans == []
    
    
    
    def isValid(self, s):
        dic = {'(': 1, ')': 2, '{': 3, '}': 4, '[': 5, ']': 6}
        ans = []
        
        for bra in s:
            if (dic[bra] % 2 == 1):
                ans.append(dic[bra])
            else:
                if (len(ans) != 0 and ans[-1] == dic[bra]-1):
                    del ans[-1]
                else:
                    return False
        return ans == []