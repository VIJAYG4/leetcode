# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = []
        stack.append((root,sum))
        
        while stack:
            node,target = stack.pop()
            target-=node.val
            
            #check if leaf node and target = 0
            if not node.left and not node.right and target==0:
                return True
            
            if node.right:
                stack.append((node.right,target))
            if node.left:
                stack.append((node.left,target))
        return False         
                     
            
                     
            
