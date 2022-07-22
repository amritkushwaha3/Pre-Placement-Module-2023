# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.recursion(root.left, root.right)

    def recursion(self, l_node,r_node):
        if l_node is None and r_node is None:
            return True
        if l_node is None or r_node is None:
            return False
        
        if l_node.val==r_node.val:  
            return self.recursion(l_node.left, r_node.right) and self.recursion(l_node.right, r_node.left)
        else:
            return False
        