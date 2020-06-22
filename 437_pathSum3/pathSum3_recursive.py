# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.numPaths = 0
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        def preOrder(node,pathsum):
            if node:
                pathsum += node.val
                
                #check if target is reached
                if pathsum == sum:
                    self.numPaths+=1
                #traverse left subtree
                preOrder(node.left,pathsum)
                #traverse right subtree
                preOrder(node.right,pathsum)
        
        def recurseTree(node):
            if node:
                preOrder(node,0)
                
                recurseTree(node.left)
                recurseTree(node.right)
                
        recurseTree(root)
        return self.numPaths
    
'''
TC: O(n^2)
SC: O(n^2)
'''    
        
