# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sametree(self, p, q):
        if p and q:
            if p.val == q.val:
                l = self.sametree(p.left, q.left)
                r = self.sametree(p.right, q.right)
                return l and r
        elif p or q:
            return False
        else:
            return True
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            if not root and not subRoot:
                return True
            return False
        
        if self.sametree(root, subRoot):
            return True
        else:
            l = self.isSubtree(root.left, subRoot)
            r = self.isSubtree(root.right, subRoot)
            return l or r
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sametree(self, p, q):
        if p and q:
            if p.val == q.val:
                l = self.sametree(p.left, q.left)
                r = self.sametree(p.right, q.right)
                return l and r
        elif p or q:
            return False
        else:
            return True
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            if not root and not subRoot:
                return True
            return False
        
        if self.sametree(root, subRoot):
            return True
        else:
            l = self.isSubtree(root.left, subRoot)
            r = self.isSubtree(root.right, subRoot)
            return l or r
