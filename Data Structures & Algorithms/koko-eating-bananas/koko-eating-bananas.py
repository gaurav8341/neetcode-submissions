class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We are running the all possible speed.
        l, r = 1, max(piles)
        res = r

        while l<=r:
            k = int((l+r)/2)

            # Finding total time for each speed. 
            total_time=0
            for p in piles:
                total_time+=math.ceil(float(p)/k)
            
            if total_time > h:
                # res=k
                l = k + 1
            else:
                # bingo got valid time to make sure the lowest possible time run again.
                res=k
                r = k - 1
            
        return res
        