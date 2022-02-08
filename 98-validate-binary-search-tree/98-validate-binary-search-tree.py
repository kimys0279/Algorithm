# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, node, minVal, maxVal):
        if node == None:
            return True
        
        if node.val <= minVal or node.val >= maxVal:
            return False
        
        left = self.helper(node.left, minVal, node.val)
        right = self.helper(node.right, node.val, maxVal)
        
        return left and right         