# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        
        if not root:
            return results
        
        queue = []
        queue.append(root)
        
        while queue:
            level_size = len(queue)
            level = []
            
            for i in range(level_size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            results.append(level)
        
        return results
        