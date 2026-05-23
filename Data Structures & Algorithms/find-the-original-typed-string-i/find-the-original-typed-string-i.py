from collections import defaultdict

class Solution:
    def possibleStringCount(self, word: str) -> int:
        # find the chars repeated 
        ## Below code will not work if non contiguous elements are repeated
        # char_count = defaultdict(lambda: 0)
        # for c in word:
        #     # if c not in char_count:
        #     char_count[c] += 1
        
        # res = 1 # original word should be counted
        # # in entire word this repaeatation might have occured only for one char 
        # for k, v in char_count.items():
        #     if v > 1:
        #         res += v - 1

        # return res

        res = 1
        prev = ''
        for c in word:
            if c == prev:
                # cnt += 1
                res += 1
            else:
                prev = c
        
        return res