# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        
        dummy.next = head
        
        prev = dummy
        
        while head != None:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head            
            head = head.next
            
        return dummy.next
        