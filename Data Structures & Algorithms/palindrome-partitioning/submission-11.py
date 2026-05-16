class Solution:

    def is_palindrome(self, s: str, l, r) -> bool:
        # This will run n/2 times where is n is len of string
        # n = len(s) - 1
        # for i in range(n//2):
        #     if s[i] != s[n-i]:
        #         return False
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

    """
        How ?
         before adding in set we need to check if substring is palindrome 
         if the total length of subset == length of string then add it in res

    """

    def partition(self, s: str) -> List[List[str]]:
        res = []

        subset = []
        def dfs(i):
            # if len(''.join(subset)) == len(s):
                # res.append(subset)
                # return
            if i >= len(s):
                res.append(subset.copy())
                return 
            
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    subset.append(s[i: j+1])
                    dfs(j+1)
                    subset.pop()
        
        dfs(0)

        return res


            
            