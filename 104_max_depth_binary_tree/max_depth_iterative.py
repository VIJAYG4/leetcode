# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        currlvlnodes = [root]
        lvlorder = []
        lvlnodes = []
        nxtlvlnodes = []
        while currlvlnodes:
            lvlnodes = []
            nxtlvlnodes = []
            for i in range(len(currlvlnodes)):
                node = currlvlnodes[i]
                lvlnodes.append(node.val)
                if node.left:
                    nxtlvlnodes.append(node.left)
                if node.right:
                    nxtlvlnodes.append(node.right)
            print(lvlnodes)
            lvlorder.append(lvlnodes)
            currlvlnodes = nxtlvlnodes    
        #print(lvlorder)
        return len(lvlorder)
                
            
