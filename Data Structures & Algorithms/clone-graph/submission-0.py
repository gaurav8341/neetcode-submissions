"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict, deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return

        oldtonew = defaultdict(lambda: Node(0))

        queue = deque()
        queue.append(node)
        oldtonew[node] = Node(node.val)
        while queue:
            curr = queue.popleft()
            # oldtonew[curr] = Node(node.val)
            for nbr in curr.neighbors:
                if nbr not in oldtonew:
                    oldtonew[nbr] = Node(nbr.val)
                    queue.append(nbr)
                oldtonew[curr].neighbors.append(oldtonew[nbr])
        
        return oldtonew[node]