import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        # while k > len
        # for x, y in points:

        #     dis = math.sqrt(x**2 + y**2)

        #     heapq.heappush(heap, (dis, [x, y]))
        
        # res = []
        # while k:
        #     (dis, pts) = heapq.heappop(heap)
        #     res.append(pts)
        #     k -= 1
        
        # return res

        ## The time complexity is nlogn for inserting points and klogn for getting values
        ## space complexity is k

        # # while k > len
        # for x, y in points:

        #     dis = math.sqrt(x**2 + y**2)
        #     heap.append((dis, [x, y]))

        # heapq.heapify(heap)
        
        # res = []
        # while k:
        #     (dis, pts) = heapq.heappop(heap)
        #     res.append(pts)
        #     k -= 1
        
        # return res



        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]
