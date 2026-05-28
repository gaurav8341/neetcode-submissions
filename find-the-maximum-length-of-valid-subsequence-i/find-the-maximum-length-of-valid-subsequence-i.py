class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # basically we need to find length of longest odd or even subsequence. 
        # We do the operation and get the x-1 array like below
        # [nums[0]+nums[1], nums[1]+nums[2], ......]
        # the length will be x-1 where x is len(nums) 
        # once we do this we just need to 
        # find longest subsequence of odd /even numbers
        # there 4 possibilities longest subsequence will be
        # all even or all odd
        # even odd or odd even
        # we need to find the longest contiguous pattern like this. 
        # and we can remove elements but not change their orders
        # we make a array of bool signifying even odd. 
        # how do we enforce pattern. We need past 2 values.

        res = 0

        for pattern in [[0, 0], [1, 1], [0, 1], [1, 0]]:
            cnt = 0
            for num in nums:
                # we actually dont need to remove anything. 
                # we just need to find which pattern is more occuring.
                if num%2 == pattern[cnt % 2]:
                    cnt += 1
                res = max(res, cnt)
        return res


        # max_len = 0
        # length = 0
        # prev = None
        # for i in range(1, len(nums)):
            
        #     curr = (nums[i-1] + nums[i]) % 2
        #     print(i, curr, prev, length, max_len)
        #     if not prev:
        #         prev = curr
        #         length += 2 # there are two thngs in a pair
        #         max_len = max(length, max_len)
        #         continue
        #     else:
        #         # check if prev and curr are equal
        #         # if they are not equal then check max and 
        #         # set length value in max_len
        #         # if they are equal then just increment max_len
        #         if prev == curr:
        #             length += 1
        #             max_len = max(length, max_len)
        #         else:
        #             length = 0
        
        # return max_len

            
