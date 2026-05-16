from heapq import *

class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        val = min(val, self.stack_min[-1] if self.stack_min else val)
        self.stack_min.append(val)
        print('push', self.stack_min)

    def pop(self) -> None:
        
        self.stack.pop()
        self.stack_min.pop()
        print('pop', self.stack_min)
       
    def top(self) -> int:
        val = None
        if self.stack:
            val = self.stack[-1]
        return val

    def getMin(self) -> int:
        # return self.
        # print(self.stack_min)
        return self.stack_min[-1]
