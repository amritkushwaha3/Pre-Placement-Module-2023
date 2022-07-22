# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.helper(root, val)
    
    def helper(self, root, val):
        if not root:
            return None
        
        if root.val == val:
            return root
        
        if val < root.val:
            return self.helper(root.left, val)
        else:
            return self.helper(root.right, val)
        
        return None
        