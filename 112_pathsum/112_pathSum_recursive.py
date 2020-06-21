# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
            self.flag = False
            
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:    
        def preOrder(root,pathSum):
            if root:
                pathSum += root.val
                
                #check for path sum
                if not root.left and not root.right:
                    if pathSum == sum:
                        self.flag = True
                    
                preOrder(root.left,pathSum)
                preOrder(root.right,pathSum)
                        
        preOrder(root,0)    
        return self.flag
                
            
