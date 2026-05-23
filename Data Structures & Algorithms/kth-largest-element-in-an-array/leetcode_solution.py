class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
            We need to implement a min heap with fixed size k.

            only insert if value is greater than root if size is full.
        """

        # heap = []

        # for n in nums:
        #     if len(heap) == k:
        #         if n > heap[0]:
        #             heapq.heappushpop(heap, n)
        #     else:
        #         heapq.heappush(heap, n)
        
        # return heap[0]

        return heapq.nlargest(k, nums)[-1]
