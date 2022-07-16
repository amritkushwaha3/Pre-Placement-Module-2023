# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        visited = set()
        
        while head and head.next:
            
            visited.add(head.val)
            
            while head.next and head.next.val in visited:
                head.next = head.next.next
            
            
            head = head.next
            
            
        return dummy.next
        