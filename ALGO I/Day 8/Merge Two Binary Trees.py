# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1, t2):
        if t1==None and t2==None:
            return None
        elif t1==None:
            return t2
        elif t2==None:
            return t1
        else:
            ans = TreeNode(t1.val+t2.val)
            ans.left=self.mergeTrees(t1.left,t2.left)
            ans.right=self.mergeTrees(t1.right,t2.right)
            return ans
        