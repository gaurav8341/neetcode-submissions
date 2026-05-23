from collections import defaultdict

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # idea is x%k will give us answer ranging from 0 to k-1
        # We get num %k for num in nums
        # we get this current rem
        # now if we want below condition to happen.
        # (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
        # we just make sure that 
        # below pattern is maintained
        # mod[0] == mod[2] == mod[4] == .. and so on
        # mod[1] == mod[3] == mod[5] == ..and so on
        # above if above condition suffices then original condition also suffices.
         
        dp = [[0] * k for _ in range(k)]
        max_len = 0

        for num in nums:
            curr_rem = num % k

            for prev_rem in range(k):
                dp[prev_rem][curr_rem] = dp[curr_rem][prev_rem] + 1
                max_len = max(max_len, dp[prev_rem][curr_rem])

        return max_len


        ### this bullshittery doesnt work
        # max_len = 0
        # max_int = None
        # parity_dict = {}#defaultdict(lambda x: 0)

        # for i in range(1, len(nums)):
        #     print(i)
        #     res = (nums[i-1] + nums[i]) % k
        #     parity_dict[res] = parity_dict.get(res, 0) + 1
        #     if max_len != 0:
        #         # we update max len and max int
        #         if parity_dict[res] > max_len:
        #             max_len = parity_dict[res]
        #             max_int = res
        #     else:
        #         max_len += 1
        #         max_int = res
        # print(max_int, max_len)
        # return max_len + 1
             