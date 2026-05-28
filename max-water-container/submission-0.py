class Solution:
    def maxArea(self, nums: List[int]) -> int:
        max_area = 0
        l, r = 0, len(nums) - 1

        # while l<r:
        for i in range(len(nums)):
            for j in range(i+1, len(nums) ):
                area = min(nums[i], nums[j]) * int(j - i)
                # print(j, i, area, nums[i], nums[j])
                max_area = max(area, max_area)

        
        return max_area
            # if 
        
        