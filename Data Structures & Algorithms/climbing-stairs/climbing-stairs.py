class Solution:
    def climbStairs(self, n: int) -> int:
        # climbing a staircase
        # n steps to top
        # each time 1 / 2 steps
        # distinct ways to climb to top

        # dp = [-1] * (n + 1)
        # dp[0] = 1 # if n =0 or n = 1 there is only one way to climb the stairs
        # dp[1] = 1

        # for i in range(2, n+1): 
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[n]

        # now i got it
        # there are how many ways to climb n stiars
        # f(n) = f(n-1) + f(n-2) + ..... + f(1)
        curr_i = 1 # if n= 1 or 0 then 1 way to climb
        prev2 = 1
        prev = 1
        for i in range(2, n+1):
            curr_i = prev2 + prev
            prev2 = prev
            prev = curr_i
        
        return curr_i
        
        # steps = 0
        # res = 0

        # def backtrack():
        #     if steps == n:
        #         res += 1
        #         return
            
        #     if n - steps:


        #     steps += 1
        #     backtrack()
        #     stesp += 1