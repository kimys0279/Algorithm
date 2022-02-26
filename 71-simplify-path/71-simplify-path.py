class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        parts = path.split('/')
        stack = []
        
        for i in parts:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return '/' + '/'.join(stack)