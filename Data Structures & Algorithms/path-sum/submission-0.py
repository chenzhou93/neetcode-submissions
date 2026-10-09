# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        currentSum = 0
        return self.backTrack(root, targetSum, currentSum)
    
    def backTrack(self, root, targetSum, currentSum):
        if root is None:
            return False
        
        currentSum += root.val
        
        # Leaf
        if root.left is None and root.right is None:
            return currentSum == targetSum
        
        if self.backTrack(root.left, targetSum, currentSum):
            return True
        if self.backTrack(root.right, targetSum, currentSum):
            return True
        
        return False
            
