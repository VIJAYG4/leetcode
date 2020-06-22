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
        
        def preOrder(root):    
            stack = []
            stack.append((root,sum))

            while stack:
                node,target = stack.pop()
                target-=node.val

                #check if target is zero
                if target == 0:
                    self.numPaths+=1
                if node.right:
                    stack.append((node.right,target))
                if node.left:
                    stack.append((node.left,target))
        
        def recurseTree(node):
            stack = []
            stack.append(node)

            while stack:
                node = stack.pop()
                preOrder(node)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
    
        recurseTree(root)
        return self.numPaths
                
        
    
'''
TC: O(n^2)
SC: O(n^2)
'''    
        
