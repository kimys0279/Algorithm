# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        
        queue = deque([root])
        num = []
        while queue:
            curr_level = []
            for _ in range(len(queue)):
                children = queue.popleft()
                if children.left:
                    queue.append(children.left)
                if children.right:
                    queue.append(children.right)
                curr_level.append(children.val)
            num.append(curr_level)
        return num
    
