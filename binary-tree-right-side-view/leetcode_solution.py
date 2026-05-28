# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            rightside = None # to hold most right node
            qlen = len(queue)

            for i in range(qlen):# this is to make sure 
            #that we are only processing nodes in current level
            # simple will be hold values in another list and 
            # extend that list in queue
                node = queue.popleft()
                if node:
                    rightside = node # in this way only the most right node will be there
                    queue.append(node.left)
                    queue.append(node.right)

            if rightside:
                res.append(rightside.val)
        return res