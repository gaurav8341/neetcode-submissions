# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        # visited = {}
        bfs = []
        queue.append(root)

        while queue:
            level = []
            # node = queue.popleft()
            qlen = len(queue)
            # bfs.append[node.val]
            for i in range(qlen):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                bfs.append(level)
                # if node.left:
                #     level.append(node.left)
                # if node.right:
                #     level.append(node.right)
        return bfs
                