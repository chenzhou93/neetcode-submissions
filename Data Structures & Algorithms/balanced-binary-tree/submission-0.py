# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height, res = self.dfs(root)
        return res
    
    def dfs(self, root):
        if root is None:
            return (0, True)
        
        left_height, is_left_balanced = self.dfs(root.left)
        right_height, is_right_balanced = self.dfs(root.right)
        condition = (is_left_balanced and is_right_balanced and abs(left_height - right_height) <= 1)
        return (max(left_height, right_height) + 1, condition)
        