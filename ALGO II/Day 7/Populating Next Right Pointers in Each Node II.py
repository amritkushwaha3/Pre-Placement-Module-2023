"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        queue=[]
        queue.append(root)
        while(len(queue)>0):
            row=[]
            cnt=len(queue)
            while(cnt>0):
                cnt-=1
                node=queue.pop(0)
                row.append(node)
                if node is None:
                    continue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            for i in range(len(row)-1):
                row[i].next=row[i+1]
            
        return root
        