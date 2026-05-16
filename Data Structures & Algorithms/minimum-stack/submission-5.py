class MinStack:
    head = None

    def __init__(self):
        pass
        

    def push(self, val: int) -> None:
        if self.head:
            self.head = Node(val, min(val, self.head.min_value), self.head)
        else:
            self.head = Node(val, val, None)

    def pop(self) -> None:
        self.head = self.head.next_node

    def top(self) -> int:
        return self.head.value

    def getMin(self) -> int:
        return self.head.min_value
    
class Node:
    def __init__(self, value, min_value, next_node):
        self.value=value
        self.min_value = min_value
        self.next_node = next_node
        
