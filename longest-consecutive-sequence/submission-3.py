class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort_nums=sorted(nums)
        # print(sort_nums)
        # max_len = min(1, len(nums))
        # len_nums = min(1, len(nums))
        # for i in range(1,len(sort_nums)):
        #     # len_nums = 0
        #     if sort_nums[i] - 1 == sort_nums[i-1]:
        #         len_nums += 1
        #         max_len=max(max_len, len_nums)
        #     elif sort_nums[i] == sort_nums[i-1]:
        #         continue
        #     else:
        #         len_nums = 1
        
        # return max_len

        nums=set(nums)
        longest=0

        for i in nums:
            if i-1 not in nums:
                length=1
                while i+length in nums:
                    length+=1
                longest=max(length, longest)
        
        return longest

        