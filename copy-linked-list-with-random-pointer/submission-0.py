"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from collections import defaultdict

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtocopy = defaultdict(lambda: Node(0))
        oldtocopy[None] = None

        curr = head 
        # we create new dict which maps the old nodes to new ones 
        # as new ones are created their value are assigned 
        # The idea is although the values and pointers will be different but address will be assigned 
        # we only need the addresses for mapping values can be asigned as we go
        while curr:
            oldtocopy[curr].val = curr.val
            oldtocopy[curr].next = oldtocopy[curr.next]
            oldtocopy[curr].random = oldtocopy[curr.random]
            curr = curr.next

        return oldtocopy[head]
