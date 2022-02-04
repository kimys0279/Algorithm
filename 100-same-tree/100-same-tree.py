# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        
        stack = [(p, q)]
        while stack:
            r1, r2 = stack.pop()
            if (r1 and not r2) or (not r1 and r2) or (r1 and r2 and r1.val != r2.val):
                return False
            
            if r1 and r2:
                stack.append((r1.left, r2.left))
                stack.append((r1.right, r2.right))
                
        return True