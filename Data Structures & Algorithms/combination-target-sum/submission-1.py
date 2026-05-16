class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []#set()
        state = []

        # def dfs(idx):
        #     if sum(state) == target:
        #         if state not in res:
        #             res.append(state.copy())
        #         return
        #     if idx >= len(nums):
        #         # state = []
        #         return
        #     if sum(state) + nums[idx] > target:
        #         return

        #     # three options 
        #     # 1. take next element
        #     # 2. Repeat the current element
        #     # 3. dont take current element.

        #     # insert current element 
        #     state.append(nums[idx])
        #     # retake current element 
        #     dfs(idx)
        #     # process next element
        #     dfs(idx+1)
        #     # Dont take current element
        #     state.pop()
        #     dfs(idx+1)

        # above will fail because on line 14 we are disregarding any element before not considering it.

        def dfs(idx, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if idx >= len(nums) or total > target:
                return

            # the below code works if we are repaeting it. as well 
            # if we are not taking repeated elem then second part will catch that case
            cur.append(nums[idx])
            dfs(idx, cur, total + nums[idx])
            cur.pop()
            dfs(idx+1, cur, total)

        dfs(0, [], 0)
        return res