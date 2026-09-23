# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    cnt = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root, k)
        return self.res
    
    def dfs(self, root, k):
        if root is None:
            return

        self.dfs(root.left, k)
        self.cnt += 1
        if self.cnt == k:
            self.res = root.val
            return
        self.dfs(root.right, k)

        