# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.sort_bst_helper(nums)
        
    def sort_bst_helper(self, nums):
        if nums == None or len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        mid = len(nums) // 2        
        root = TreeNode(nums[mid])
        
        root.left = self.sort_bst_helper(nums[0: mid])
        root.right = self.sort_bst_helper(nums[mid + 1 : len(nums)])
        
        return root
        