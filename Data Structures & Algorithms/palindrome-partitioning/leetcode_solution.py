# class Solution:

    # def is_palindrome(self, s: str, l, r) -> bool:
    #     # This will run n/2 times where is n is len of string
    #     # n = len(s) - 1
    #     # for i in range(n//2):
    #     #     if s[i] != s[n-i]:
    #     #         return False
    #     while l < r:
    #         if s[l] != s[r]:
    #             return False
    #         l, r = l + 1, r - 1
    #     return True

    # def partition(self, s: str) -> List[List[str]]:
    #     res = []

    #     subset = []
    #     def dfs(i):
    #         # if len(''.join(subset)) == len(s):
    #             # res.append(subset)
    #             # return
    #         if i >= len(s):
    #             res.append(subset.copy())
    #             return 
            
    #         for j in range(i, len(s)):
    #             if self.is_palindrome(s, i, j):
    #                 subset.append(s[i: j+1])
    #                 dfs(j+1)
    #                 subset.pop()
        
    #     dfs(0)

    #     return res

"""
In below soln we precaclculate if string is palindorme or not

"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True

        def backtrack(start, path):
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if dp[start][end]:
                    backtrack(end + 1, path + [s[start:end+1]])

        result = []
        backtrack(0, [])
        return result
            
            