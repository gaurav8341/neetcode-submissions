class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = set()

        def backtrack(state, nums, taken):
            if len(state) == len(nums):
                print(state)
                res.add(tuple(state))
                return

            for i in range(len(nums)):
                if taken[i]:
                    continue
                taken[i] = True
                state.append(nums[i])
                backtrack(state, nums, taken)
                taken[i] = False
                state.pop()
                    
        backtrack([], nums, [False] * len(nums))

        return [list(st) for st in res]
            

