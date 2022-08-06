# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        
        if not root:
            return results
        
        queue = []
        queue.append(root)
        
        
        level_index = 0
        
        while queue:
            
            size = len(queue)
            level = []
            
            for i in range(size):
                node = queue.pop(0)
                if level_index % 2 != 0:
                    level.insert(0, node.val)
                else:
                    level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            results.append(level)
            level_index += 1
                
        return results
        