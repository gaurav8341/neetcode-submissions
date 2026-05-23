# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val:idx for idx, val in enumerate(inorder)}

        self.post_idx = len(postorder) - 1

        def dfs(l, r):
            if l> r: 
                return None
            # print(self.post_idx)
            root_val = postorder[self.post_idx]
            mid = idx_map[root_val]
            self.post_idx -= 1
            root = TreeNode(root_val)
            # here first right then left because of postorder structure
            root.right = dfs(mid+1, r)
            root.left = dfs(l, mid - 1)
            
            return root
        
        return dfs(0, len(inorder) - 1)