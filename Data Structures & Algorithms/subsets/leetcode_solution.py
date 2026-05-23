class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # here Parse through the list.
        # with one main elem lets say one at oth position.
        # Backtracking means i need to come back and remove certain elem.
        # DFS

        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # We have two choices take current value or not.
            # 2. take
            subset.append(nums[i])
            dfs(i+1)
            # 1. dont take
            # The reason we dont take first is lates on the same subset is used in next functions as well. 
            # memory issue is happening.
            subset.pop()
            dfs(i+1)

            

        dfs(0)
        return res


     