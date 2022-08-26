# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        self.helper(root, ret)
        return ret
    
    def helper(self, root, ret):
        if not root:
            return 0
        left = self.helper(root.left, ret)
        right = self.helper(root.right, ret)
        lvl = max(left, right) + 1
        
        if lvl > len(ret):
            ret.append([])
        ret[lvl - 1].append(root.val)
        
        return lvl