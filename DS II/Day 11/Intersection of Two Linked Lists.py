# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        a = headA
        b = headB

        while a != b:
            a = headB if a == None else a.next
            b = headA if b == None else b.next

        return a
        