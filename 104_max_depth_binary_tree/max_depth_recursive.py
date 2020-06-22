# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.depths = []
        
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def preOrder(root,depth):
            if root:
                depth+=1
                
                #check if leaf node
                if not root.left and not root.right:
                    self.depths.append(depth)
                
                preOrder(root.left,depth)
                preOrder(root.right,depth)
                
        preOrder(root,0)
        return max(self.depths)
        
        
            
            
            
            
        
