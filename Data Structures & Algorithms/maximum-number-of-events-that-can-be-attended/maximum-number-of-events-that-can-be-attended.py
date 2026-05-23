import functools

import heapq 

class Solution:

    def maxEvents(self, events: List[List[int]]) -> int:
        # first sort the events along the first day
        events.sort()

        min_heap = []

        d = 0 # current day
        index = 0 # index of events araay
        result = 0
        n = len(events)

        while min_heap or index < n:
            if not min_heap:
                # minheap is null
                # either it is start or there is gap of says betwn events
                # anyway 
                d = events[index][0]

            while index < n and events[index][0] <= d:
                # day is greater than equal to events[idx] last day
                heapq.heappush(min_heap, events[index][1])
                index += 1
            
            heapq.heappop(min_heap)
            result += 1
            d += 1
            
            while min_heap and min_heap[0] < d:
                heapq.heappop(min_heap)

        return result
            



    # def maxEvents(self, events: List[List[int]]) -> int:
        # return maximum events that can be attended.

        # Lets Sort the events along the startday

        # def compare_events(e1, e2):
        #     ## return if first arg is less than 2

        #     if e1[0] < e2[0]:
        #         return -1
        #     elif e1[0] == e2[0]:
        #         if e1[1] < e2[1]:
        #             return -1
        #         elif e1[1] == e2[1]:
        #             return 0 
        #     return 1

        # events.sort(key=functools.cmp_to_key(compare_events))

        # start_day, last_day = events[0][0], events[-1][1]

        # print(events, start_day, last_day)


        # result = 0
        # idx = 0
        # n = len(events)
        # i = start_day
        # # for i in range(start_day, last_day+1):
        # while i <= last_day and idx < n:
        
        #     print(i, events[idx], i in range(events[idx][0], events[idx][1]+1))
        #     if events[idx][0] <= i <= events[idx][1]:
        #         result += 1
        #         idx += 1 
        #         i += 1
        #     elif i > events[idx][1]:
        #         idx += 1
        #         # event should not increament here
        #     elif i < events[idx]:
        #         i += 1
        #         # index should not increament
            
        # return result