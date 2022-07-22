# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.helper(root)
        
        
    def helper(self, root):
        if not root:
            return root
        
        if not root.left and not root.right:
            return root
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        root.left = right
        root.right = left
        
        return root
        