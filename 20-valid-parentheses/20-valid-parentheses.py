class Solution(object):
    def isValid(self, s):
        
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
            
        return stack == []