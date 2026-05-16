import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k

        # for i in nums:
        heapq.heapify(self.heap)
        
        while k < len(self.heap):
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:

        try:
            min_num=self.heap[0]
        except IndexError:
            min_num = -1001
        # only add element if eleemnet is geater than smallest umber
        if min_num < val and len(self.heap) == self.k:
            heapq.heappop(self.heap)

        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)

        return self.heap[0]
