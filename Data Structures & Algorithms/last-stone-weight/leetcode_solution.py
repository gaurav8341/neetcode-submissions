import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # the implementation of max heap isnt there

        heapq.heapify(stones)

        # for s in stones:
            # heapq.heappush

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            
            diff = abs(s1-s2) * -1

            if diff != 0:
                heapq.heappush(stones, diff)
        
        stones.append(0) # return 0 if nothing
        return abs(stones[0]) # we have saved values in

