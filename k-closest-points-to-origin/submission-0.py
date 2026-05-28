import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        # while k > len
        for x, y in points:

            dis = math.sqrt(x**2 + y**2)

            heapq.heappush(heap, (dis, [x, y]))
        
        res = []
        while k:
            (dis, pts) = heapq.heappop(heap)
            res.append(pts)
            k -= 1
        
        return res