# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getdepth(self, root: Optional[TreeNode], k:int) -> int:
        if not root:
            return k
        return max(self.getdepth(root.left, k+1),
                    self.getdepth(root.right, k+1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getdepth(root, 0)