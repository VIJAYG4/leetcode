# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack=[]
        curr = root
        inorder = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            inorder.append(curr.val)
            curr = curr.right
        return inorder    
            
        
'''
TC: O(n)
SC: O(n)
'''

