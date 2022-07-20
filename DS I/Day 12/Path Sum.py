# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False 
        
        if root.val == sum:            
            if root.left == None and root.right == None:
                return True
            else:
                return self.hasPathSum(root.left ,0 ) or self.hasPathSum(root.right ,0)                 
        else:
            leftover = sum - root.val
            return self.hasPathSum(root.left , leftover) or self.hasPathSum(root.right, leftover)
        