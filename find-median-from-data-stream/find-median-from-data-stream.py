import heapq
class MedianFinder:

    def __init__(self):
        self.left_heap = [] # will have left half --  max heap 
        self.right_heap = [] # will have right half -- min heap
        # self.counter = 0
        # print(self.counter) ## debug only
        # Boths' size diff should not be more than 1

    def addNum(self, num: int) -> None: 
        # print(f"============Add num: {num}================")
        # self.counter+=1
        # if self.left_heap and self.right_heap:
        #     if num > (self.left_heap[0] * -1):
        #         # insert in rightheap
        #         heapq.heappush(self.right_heap, num)
            
        #     if num <= self.right_heap[0]:
        #         # insert in left heap
        #         heapq.heappush(self.left_heap, (num*-1))
        # else:
        #     # by default insert in left heap
        #     # we will conitnuously check for imbalance 
        #     # so when imbalance becomes 2 then balancing happen
        #     heapq.heappush(self.left_heap, (num*-1))

        if self.right_heap and num > self.right_heap[0]:
            heapq.heappush(self.right_heap, num)
        else:
            heapq.heappush(self.left_heap, num*-1)


        # although the way we are desingning 
        # there cant be imabalnce of more than 2
        # but nonetheless this code should be enclosed in while loop.

        left_size, right_size = len(self.left_heap), len(self.right_heap)
        diff = left_size - right_size
        while abs(diff) > 1:
            # only balance if imbalance is greater than 1.
            if diff < -1:
                # right side elements should be moved to left
                elem = heapq.heappop(self.right_heap)
                heapq.heappush(self.left_heap, (elem*-1))
            if diff > 1:
                # left side content should be moved to right
                elem = heapq.heappop(self.left_heap) 
                heapq.heappush(self.right_heap, (elem*-1))
            
            left_size, right_size = len(self.left_heap), len(self.right_heap)
            diff = left_size - right_size
        
        # print("left_heap", self.left_heap)
        # print("right_heap", self.right_heap)
        # print(f"==============={self.counter}=============")

        
    def findMedian(self) -> float:
        # print("=================Find Median===============")
        left_size, right_size = len(self.left_heap), len(self.right_heap)
        diff = left_size - right_size
        if not diff:
            left_elem = self.left_heap[0] * -1
            right_elem = self.right_heap[0]
            return (left_elem + right_elem) / 2.0
        else:
            # array was odd sized
            if diff < 0:
                # middle element is at right
                return self.right_heap[0]
            if diff > 0:
                return self.left_heap[0] * -1
            
        
        