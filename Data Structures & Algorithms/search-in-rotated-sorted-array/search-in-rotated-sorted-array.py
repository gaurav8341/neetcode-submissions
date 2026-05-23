class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2

            if target == nums[m]:
                return m

            # if l <= m then its normal left subpart. 
            if nums[l] <= nums[m]:
                # Here 2nd condition is very logical for binary search
                # 1st condition: if target < l then target is in rotated right part.
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else: 
                # normal part
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1

# if above solution is too hard remember that you can run it in 2 pass.

# in first pass find the pivot where array is rotated. normal array wont fulfill condition m > r

# you will find pivot now depending on pivot and target value run binary search on appropriate subarray.