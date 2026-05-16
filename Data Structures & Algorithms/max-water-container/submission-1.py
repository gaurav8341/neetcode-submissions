class Solution:
    def maxArea(self, nums: List[int]) -> int:
        area = 0
        l, r = 0, len(nums) - 1

        # 
        while l < r:
            area = max(min(nums[l], nums[r]) * (r - l), area)

            if nums[l] < nums[r]:
                l+=1
            elif nums[l] >= nums[r]:
                r-=1


        
        return area
            # if 
        
        