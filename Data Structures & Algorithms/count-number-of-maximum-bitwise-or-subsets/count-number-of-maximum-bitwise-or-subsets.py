class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # find  max possble bitwise 
        # The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
        # We need to find the subset with max of above value.
        # how to get max. 
        # max bitwise or is bitwise or of whole array.

        # find bitwise or of whole array
        arr_bit_or = 0
        for n in nums:
            arr_bit_or |= n 

        # we got max arr_bit_or

        # now backtracking
        count = 1 # the original array is one

        def backtrack(bit_or, i):
            nonlocal count
            if i >= len(nums):
                return 1 if bit_or == arr_bit_or else 0
            # below condition will stop when we get the answer. Little bit optimization
            if bit_or == arr_bit_or:
                # count += 1
                # if we reach until this point then all remaining array points will be valid 
                # 1 << x  == 2 ** x
                # at each point we make 2 choices so we can also replace below code with
                return 2 ** (len(nums) - i)#1 << (len(nums) - i)

            
            return backtrack(bit_or | nums[i], i+1) + backtrack(bit_or, i+1)
        
        return backtrack(0, 0)