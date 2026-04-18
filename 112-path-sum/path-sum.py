class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
        
        remaining = targetSum - root.val
        
        if root.left:
            if self.hasPathSum(root.left, remaining):
                return True
        
        if root.right:
            if self.hasPathSum(root.right, remaining):
                return True
        
        return False