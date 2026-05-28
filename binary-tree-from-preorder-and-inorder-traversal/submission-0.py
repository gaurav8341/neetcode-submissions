# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder root, left, right
        # inorder left, root, right

        # from preorder we will get root 
        # but left and right subtree we will get from inorder partitions
        inndx = {val:idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0 # we will increament this every iteration
        def dfs(l, r):
            """
                l: left bound 
                r: right bound
            """
            if l>r:
                # we are doing this to avoid index error
                return None
            

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            in_partition = inndx[root_val]
            root = TreeNode(root_val)
            root.left = dfs(l, in_partition-1)
            root.right = dfs(in_partition+1, r)

            return root
        
        return dfs(0, len(inorder) - 1)