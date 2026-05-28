# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:

    
    def inorder(self, root,last_elem=None):
        if not root:
            return 
        
        self.inorder(root.left)
        # print(inorder)
        self.arr.append(root.val)
        self.inorder(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        self.inorder(root)
        return self.arr[k-1]

