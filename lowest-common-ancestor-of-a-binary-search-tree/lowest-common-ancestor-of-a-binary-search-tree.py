# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # this is a bst in bst left is less than root and 
        # right is more than root
        # in case if p>root>q or q>root>p then root is anser
        # else got through the tree

        if not root or not p or not q:
            return None

        p_val, q_val, root_val = p.val, q.val, root.val
        if p_val > root_val and q_val > root_val:
            # LCA is at right of root
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < root_val and q_val < root_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
