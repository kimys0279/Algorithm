class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = 0
        string = ''
        stack = []
        
        for c in s:
            if c.isalnum():
                if c.isdigit():
                    num = num*10 + int(c)
                elif c.isalpha():
                    string += c
            
            elif c == '[':
                stack.append(string)
                stack.append(num)
                string = ''
                num = 0
            elif c == ']':
                pre_num = stack.pop()
                pre_string = stack.pop()
                string = pre_string + pre_num * string
        return string