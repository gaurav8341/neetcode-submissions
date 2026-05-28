class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        prev = 0
        curr = 1
        nextt = 2

        cnt = 0

        while nextt < len(nums):
            while nextt < len(nums) and nums[curr] == nums[nextt]:
                nextt += 1
            
            if nextt >= len(nums): break

            if (nums[curr] > nums[prev] and nums[curr] > nums[nextt]) or \
                (nums[curr] < nums[prev] and nums[curr] < nums[nextt]):
                cnt += 1
            prev = curr
            curr = nextt
        
        return cnt