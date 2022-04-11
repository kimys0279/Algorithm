# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        
        def dfs(node, mx):
            if not node: return 0
            
            res = 1 if node.val >= mx else 0
            
            mx = max(mx, node.val)
            res += dfs(node.left, mx)
            res += dfs(node.right, mx)
            return res
        
        return dfs(root, root.val)