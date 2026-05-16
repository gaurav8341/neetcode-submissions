class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        min_nums = max(nums[l], nums[r])

        while l <= r:
            m = int((l+r)/2) 
            if nums[l] < nums[r]:
                min_nums = min(nums[l], min_nums)
                break
            # print(l, r, m, nums[l], nums[r], nums[m], min_nums)
            min_nums = min(min_nums, nums[m])
            # we need to find where the min elem might be
            
            if nums[m] >= nums[l]:
                # the min value is at right
                l = m+1
            else:
                # the min value is at left
                r = m-1
        
        # print(l, min_nums)
        return min_nums