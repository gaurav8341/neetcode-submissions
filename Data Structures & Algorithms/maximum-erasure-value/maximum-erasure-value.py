class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # delete sub array
        # all elems in sub array should be unique
        # get max score, wcore is addition on all elem in  subarray

        # sliding window of variable size
        # if we find any elem which is repeated 
        # then new lower boiund of sub array is elem_idx which is repeated + 1 

        # lets do simple approach first
        subarray = set()
        count, max_count = 0, 0
        l = 0# we only need one index below i would act as our right idx
        for i in range(len(nums)):
            # c = nums[i]
            # check if c is in subarray
            # if c in subarray:
                # c is in subarray
                # we take old idx
                # new_l = subarray[c] + 1
            while nums[i] in subarray:
                count -= nums[l]
                subarray.remove(nums[l])
                l += 1
                # l += 1
                # now we have new l 
            # below operation should be performed in any case
            subarray.add(nums[i])
            count += nums[i]
            max_count = max(count, max_count)
        
        return max_count