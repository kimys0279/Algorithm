# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def levelOrder1(self, root):
        if not root:
            return []
        
        ans = []
        q = collections.deque([root])
        
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
              ans.append(level)
            
        return ans
    
    
    
    def levelOrder(self, root):
        if not root:
            return []
        
        q = collections.deque([root])
        ans = []
        
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
            if level:
                ans.append(level)
        return ans
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    