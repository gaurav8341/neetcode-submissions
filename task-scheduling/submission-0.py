from collections import deque, Counter

import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque() # this is a queue of task last processed. 

        # we will process the most frequent element first.
        # there needs to be a cooldown period of n count . we can have this either by dict(list if we want to be efficient)
        # Before that we need to build the heap. and update the heap according to count. # this is most difficult as we need to 

        count = Counter(tasks) 
        maxheap = [-cnt for cnt in count.values()] #python only has minheap implementation
        heapq.heapify(maxheap)

        time = 0

        while maxheap or q:
            time += 1

            if maxheap:
                # get max  element and update the count in que
                cnt = 1 + heapq.heappop(maxheap) # remember how we are impleenting the maxheap look at line 14
                if cnt:
                    q.append([cnt, time+n]) # we will readd at this time in heap
            # else:

            if q:
                if q[0][1] == time:
                    heapq.heappush(maxheap, q.popleft()[0])
        
        return time