class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        op = []
        # max_num = float("-infinity")
        r = l = 0
        dq = collections.deque() 
        # dq wont allow right most elemnt > left elements 

        for r in range(len(nums)):
            # make 
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            
            dq.append(r)

            # this is thereason we are using indices 
            # we need to remove values if they are ot in current window
            if l > dq[0]:
                dq.popleft()

            # why do we have this condition 
            if r-l+1 >= k:
                op.append(nums[dq[0]])
                # dq.pop()
                l += 1

        
        return op 