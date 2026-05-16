# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # we have three choices either take left side , right side or 
        # no split ie. take only root

        # res = -float('inf')
        res = [root.val]

        def dfs(root):
            # nonlocal res
            if not root:
                return 0

            leftMax = max(0, dfs(root.left))
            rightMax = max(0, dfs(root.right))

            # what is max whether non split is max or parent node is max
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        dfs(root)

        return res[0]

