# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:        
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        stack = []
        stack.append((root,sum,[root.val]))
        paths = []
        
        while stack:
            node,target,path = stack.pop()
            target-=node.val
            
            #check if leaf node and target=0
            if not node.left and not node.right and target==0:
                paths.append(path) 
            if node.right:
                stack.append((node.right,target,path+[node.right.val]))
                
            if node.left:
                stack.append((node.left,target,path+[node.left.val]))
        
        return paths
            
            
        
                        
        
