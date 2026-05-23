class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        subset = []

        nums.sort() # we will have sorted nums

        def dfs(subset, idx):
            # we dont want duplicate subsets
            # check for duplicate subset and insert if no
            # print(subset, res, tuple(set(subset)) not in res)
            # if tuple(set(subset)) not in res: # we will add empty list later
                # res.add(tuple(subset))

            res.append(subset[::])

            for jdx in range(idx, len(nums)):
                if jdx > idx and nums[jdx] == nums[jdx - 1]:
                    # avoid duplicate numbers
                    continue
                subset.append(nums[jdx])
                dfs(subset, jdx + 1)
                subset.pop()
        
        dfs([], 0)

        return res#[list(t) for t in res]
        

