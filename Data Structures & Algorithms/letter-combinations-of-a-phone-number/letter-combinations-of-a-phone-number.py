class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_char = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        res = []

        # global charset
        # charset = ""

        def dfs(i, charset):
            if i >= len(digits):
                if charset:
                    res.append(charset)
                return
            
            for c in num_char[digits[i]]:
                # charset = c
                dfs(i+1, charset+c)
                # charset = charset[:-1]
        
        dfs(0, "")

        return res


        

        
