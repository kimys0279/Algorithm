class Solution(object):
    def minAddToMakeValid1(self, s):
        """
        :type s: str
        :rtype: int
        """
        while "()" in s:
            s = s.replace('()', "")
        return len(s)
    
    def minAddToMakeValid(self, s):
        l, r = [], 0
        for i in s:
            if i == '(':
                l.append(i)
            elif l:
                l.pop()
            else:
                r += 1
        return r + len(l)