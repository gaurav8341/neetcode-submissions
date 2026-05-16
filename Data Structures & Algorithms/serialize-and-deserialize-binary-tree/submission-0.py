# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            # nonlocal res
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.idx = 0

        def dfs():
            # nonlocal vals
            if vals[self.idx] == "N":
                self.idx += 1
                return None

            node  = TreeNode(int(vals[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

