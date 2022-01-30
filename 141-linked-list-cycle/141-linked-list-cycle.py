# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        visited = set()
            
        while head != None:
            if head not in visited:
                visited.add(head)
            else:
                return True
            
            head = head.next
            
        return False