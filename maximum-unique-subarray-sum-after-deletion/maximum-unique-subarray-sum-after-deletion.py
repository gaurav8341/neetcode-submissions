class Solution:
    def maxSum(self, nums: List[int]) -> int:

        s=0
        for i in set(nums) :
            if i >0:
                s+=i
        if s==0:
            return max(nums)
        return s
        # max_sum = 0
        # summ = 0
        # res = set()
        # # for n in nums:
        # #     if n not in res:
        # #         max_sum += n
        # #         res.add(n)
        # # while 
        # # make element count dict from nums array. 
        # # sort it along keys in decreasing order
        # # if we take any element we decrement the count
        # # dont empty entire array. ie atlest one elem in dict
        # num_dict = dict()
        # for n in nums:
        #     if n not in num_dict:
        #         num_dict[n] = 0
        #     num_dict[n] += 1
        
        # for key in sorted(num_dict.keys(), reverse=True):
        #     if key in res:
        #         continue
        #     # key not in res
        #     # check if max_sum will increase if not continue
        #     if max_sum + key <= max_sum:
        #         continue
        #     # check the size of dict
        #     if len(num_dict) == 1:
        #         # check if count of one elem
        #         if key in num_dict and num_dict[key] <= 1:
        #             continue
            
        #     num_dict[key] -= 1
        #     if num_dict[key] == 0:
        #         num_dict.pop(key, None)
        #     max_sum = max_sum + key


        # return max_sum