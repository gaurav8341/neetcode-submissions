class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []#  set()

        candidates.sort()
        # state = []

        def dfs(idx, state, cur):
            if cur == target:
                # if state not in res:
                # res.add(tuple(state))
                res.append(state.copy())
                return 
            
            if idx >= len(candidates) or cur > target:
                return
            # if we are to use set for this then we need to store idx and value
            state.append(candidates[idx])
            dfs(idx+1, state, cur + candidates[idx])
            state.pop()
            # we are doing this because if same elemnt is being processed agin then it wont affect anything. but we will be doing repeat calculations
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            dfs(idx+1, state, cur)
        
        dfs(0, [], 0)
        return [list(st) for st in res]