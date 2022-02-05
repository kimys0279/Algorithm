# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        if not root:
            return None
        
        if root.left == None and root.right == None:
            return root.val
        
        lowest = root
        leftseq = [root]
        
        while lowest.left != None:
            lowest = lowest.left
            leftseq.append(lowest)
            
        leftseq.pop()
        
        while k > 1:
            if lowest.right==None:
                    lowest=leftseq.pop()
            else:
                lowest=lowest.right
                while lowest.left!=None:
                    leftseq.append(lowest)
                    lowest=lowest.left
            k-=1
        return lowest.val