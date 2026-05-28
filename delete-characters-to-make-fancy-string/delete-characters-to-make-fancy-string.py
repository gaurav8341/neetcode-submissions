class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""

        prev = None
        count = 1
        for c in s:
            # print(c, prev, count)
            if c != prev:
                count = 1
                prev = c
                res += c
            else:
                # check if count > 2
                count += 1
                if count > 2:
                    continue
                else:
                    res += c
        
        return res