class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # max possible bitwise and
        # and will always be less than the max of the numbers involved
        # eg 3&1 =  1
        # 3&2 = 2
        # 4&3 = 2
        # 4&4 = 4
        # 4&4&3 = 2
        # 4&4&1 = 0
        # inshort the question is to find the largest subarray contaning the max element.
        # max_elem = 0
        # max_count, count = 0, 0
        # for  i in nums:
        #     if i > max_elem:
        #         # new max is found also reset the max_count
        #         max_elem = i
        #         count = 0
        #         max_count = 0
            
        #     if i < max_elem:
        #         count = 0
        #     elif i == max_elem:
        #         count += 1

        #     max_count = max(max_count, count)


        # return max_count
        # aaperently O(2*n) is faster than above O(n) approach
        maxi = max(nums)
        max_len = 0
        length = 0

        for num in nums:
            if num == maxi:
                length += 1
                max_len = max(max_len, length)
            else:
                length = 0

        return max_len
