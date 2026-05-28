# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isvalid(self, node, lowerlimit, upperlimit):
        if not node:
            return True
        
        l = node.left
        r = node.right
        if upperlimit > node.val > lowerlimit:
            return self.isvalid(node.left, lowerlimit, node.val) and self.isvalid(node.right, node.val, upperlimit)
        else: 
            return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.isvalid(root, float('-infinity'), float('infinity'))
        # if not root:
        #     return True

        # l = root.left
        # r = root.right
        
        # if not l and not r:
        #     return True
        
        # if l:
        #     if l.val >=root.val:
        #         return False
        
        # if r:
        #     if r.val <= root.val:
        #         return False
        
        # return self.isValidBST(l) and self.isValidBST(r)