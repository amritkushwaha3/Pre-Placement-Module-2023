# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t == None and s == None:
            return True
        if t == None or s == None:
            return False
        if s.val == t.val and self.rootSubtree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def rootSubtree(self, s, t):
        if t == None and s == None:
            return True
        if t == None or s == None or s.val != t.val:
            return False
        return self.rootSubtree(s.left, t.left) and self.rootSubtree(s.right, t.right)
        