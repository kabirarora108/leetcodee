# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Leaf node (no children)
        if not root.left and not root.right:
            return 1
        
        # Node has only right child
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # Node has only left child  
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # Node has both children - take minimum
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))