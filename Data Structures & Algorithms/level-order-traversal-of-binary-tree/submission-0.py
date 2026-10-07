# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque()

        if root is None:
            return []
        
        dq.append(root)

        tmp_list = []
        res = []

        while len(dq) > 0:
            n = len(dq)
            #print('n', n)
            tmp_list = []
            for i in range(n):
                node = dq.popleft()

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
                tmp_list.append(node.val)

            res.append(tmp_list)    
        
        return res
            


        