# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        count = 0
        
        fast = head
        while fast != None:
            fast = fast.next
            count += 1
        
        mid = count // 2 + 1
        
        slow = head
        for i in range(1, mid):
            slow = slow.next
            
        return slow
        