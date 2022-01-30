# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        #간편하게 return head.reverse(), reversed(head), head[::-1] 가 안먹히는 이유는??
        
        prev, curr = None, head  
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr 
            curr = nxt
        return prev
    