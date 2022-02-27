class Solution(object):
    def isPalindrome(self, s):
        
        if len(str(s)) == 0:
            return True
        
        new = ''
        s = s.lower()
        
        for i in s:
            if i.isalnum():
                new = new + i
            
        return new == new[::-1]
    
    
    
    def isPalindrome(self, s):
        if len(str(s)) == 0:
            return True
        
        new = ''
        s = s.lower()
        
        for i in s:
            if i.isalnum():
                new = new + i
        return new == new[::-1]