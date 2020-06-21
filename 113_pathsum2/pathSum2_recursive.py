# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
            self.paths = []
            
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def preOrder(root,pathSum,path):
            if root:
                path.append(root.val)
                pathSum += root.val
                
                #check if leaf node
                if not root.left and not root.right:
                    if pathSum == sum:
                        #print(pathSum,path)
                        #trick: appending list(path) does the trick
                        self.paths.append(list(path))
                        #print(self.paths)
                preOrder(root.left,pathSum,path)
                preOrder(root.right,pathSum,path)
                del path[-1]
                
        preOrder(root,0,[])
        return self.paths
                        
        
