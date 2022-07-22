# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        s = [root]
        while s:
            temp = s.pop()
            res.append(temp.val)
            if temp.right:
                s.append(temp.right)
            if temp.left:
                s.append(temp.left)
        return res
        