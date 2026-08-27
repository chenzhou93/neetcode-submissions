# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMaxFromLeftSubTree(self, root):
        cur = root
        while cur and cur.right:
            cur = cur.right
        return cur


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                maxNode = self.findMaxFromLeftSubTree(root.left)
                tmpVal = maxNode.val
                root.val = maxNode.val
                root.left = self.deleteNode(root.left, tmpVal)
                return root
        
        return root

        