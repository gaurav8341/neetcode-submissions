
"""
Diagram only:
https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/solutions/1747029/python-explanation-with-pictures-priority-queue
"""
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n3 = len(nums)
        n = n3 // 3
        
        # to get the min diff. we basically need to 
        #     1. extract largest numbers from left part
        #     2. extract smallest numbers fro  right part

        prefix_heap = [-v for v in nums[:n]]# max heap of first n elems
        heapq.heapify(prefix_heap)
        left_sum = sum(nums[:n])# sum of left part array
        prefix_sum = [left_sum] # prefix sum array

        right_sum = sum(nums[2*n:]) # sum of right part array
        suffix_sum = [right_sum]
        suffix_heap = [v for v in nums[2*n:]]# min heap of first n elems
        heapq.heapify(suffix_heap)

        # We did the job of extreme ends of array. 
        # mid part still in contention

        for i in range(n, 2*n):
            if nums[i] < -prefix_heap[0]:
                left_sum += nums[i] + prefix_heap[0]
                heapq.heappop(prefix_heap)
                heapq.heappush(prefix_heap, -nums[i])
            prefix_sum.append(left_sum)
            
        
        for i in range(2*n-1, n-1, -1):# range(n, 2*n)
            if nums[i] > suffix_heap[0]:
                right_sum += nums[i] - suffix_heap[0]
                heapq.heappop(suffix_heap)
                heapq.heappush(suffix_heap, nums[i])
            suffix_sum.append(right_sum)
        suffix_sum = suffix_sum[::-1]

        ans = math.inf
        print(prefix_sum, suffix_sum)
        for a, b in zip(prefix_sum, suffix_sum):
            ans = min(ans, a - b)
        return ans 
    # def minimumDifference(self, A: List[int]) -> int:
    #     n = len(A) // 3
        
    #     # Build pre_min using min-heap.
    #     pre_min, cur_min = [sum(A[:n])], sum(A[:n])
    #     pre_hp = [-x for x in A[:n]]
    #     heapq.heapify(pre_hp)
    #     for i in range(n, 2 * n):
    #         print(i)
    #         cur_pop = -heapq.heappop(pre_hp)
    #         cur_min -= cur_pop
    #         cur_min += min(cur_pop, A[i])
    #         pre_min.append(cur_min)
    #         heapq.heappush(pre_hp, -min(cur_pop, A[i]))          
        
    #     # Build suf_max.
    #     suf_max, cur_max = [sum(A[2*n:])], sum(A[2*n:])
    #     suf_hp = [x for x in A[2*n:]]
    #     heapq.heapify(suf_hp)        
    #     for i in range(2 * n - 1, n - 1, -1):
    #         print(i)
    #         cur_pop = heapq.heappop(suf_hp)
    #         cur_max -= cur_pop
    #         cur_max += max(cur_pop, A[i])
    #         suf_max.append(cur_max)
    #         heapq.heappush(suf_hp, max(cur_pop, A[i]))
    #     suf_max = suf_max[::-1]
        
    #     # Iterate over pre_min and suf_max and get the minimum difference.
    #     ans = math.inf
    #     print(pre_min, suf_max)
    #     for a, b in zip(pre_min, suf_max):
    #         ans = min(ans, a - b)
    #     return ans 
