# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # using modified DFS 
    # where one function sends the height to  be 
    # used by bottom stack f-calls
    # balanced tree have max diff of 1 in the height of two nodes more than 
    # that and its imbalanced tree 
    # we also need to make sure the above tree is balanced
    def height(self, root):
        if not root:
            return 0, True

        # height = height + 1
        l_h, l_t =  self.height(root.left)
        r_h, r_t = self.height(root.right)
        diff = abs(l_h - r_h)
        return  1 + max(l_h, r_h), (diff <= 1) and l_t and r_t 

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        _, balance = self.height(root)

        return balance
        