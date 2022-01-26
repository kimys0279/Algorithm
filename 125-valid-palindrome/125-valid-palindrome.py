class Solution(object):
    def isPalindrome(self, s):
        
        new = ''
        s = s.lower()
        
        for i in s:
            if i.isalnum():
                new = new + i
                
        return new == new[::-1]