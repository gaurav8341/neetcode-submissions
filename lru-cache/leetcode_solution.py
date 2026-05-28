class Node:
    def __init__(self, key:int = None, val:int = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
"""
In LRU at put and the entry will be created 
at get its position will be changed
In the kvdict we should have the node instead of int in value 
to get o(1) insertion and deletion from LL 

"""
class LRUCache:

    def __init__(self, capacity: int):
        self.kvdict = {}
        self.capacity = capacity
        self.length = 0
        self.head = Node(0, 0)
        self.last = Node(0, 0)
        self.last.prev, self.head.next = self.head, self.last
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        # insert node at beginning
        # node = Node(key, value)
        prev, nxt = self.last.prev, self.last
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.kvdict:
            self.remove(self.kvdict[key])
            self.insert(self.kvdict[key])
            return self.kvdict[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kvdict:
            self.remove(self.kvdict[key])
        self.kvdict[key] = Node(key, value)
        self.insert(self.kvdict[key])

        if len(self.kvdict) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.kvdict[lru.key]
        
