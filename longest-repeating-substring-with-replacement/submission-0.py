import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # recent_char = ''
        # max_len = 0
        # no_rep = 0 # count of no repetition.
        # for c in s:
        return self.sliding_window(s, k)
    
    def brute_force(self, s:str, k:int)->int:
        res = 0

        for i in range(len(s)):
            freqdict = dict()

            for j in range(i, len(s)):
                freqdict[s[j]] = freqdict.get(s[j], 0) + 1
                # we will consider the most repeated character 
                # as main chanracter and will replace other chars
                # we want to send the overall result 
                # so dict isnt necessary
                # The length of substring will be j 
                # ie inner loops pointer(right pointer)
                # i is left pointer
                # j-i + 1 is len of substring 
                # if maxlen - max frequency <= k is valid case
                if j - i + 1 - freqdict[s[j]] <= k:
                    res = max(res, j - i + 1)
        return res

    def sliding_window(self, s:str, k:int) -> int:
        res = 0

        maxf = 0
        l = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            while r - l + 1 - maxf > k:
                # in case of negative scenario we stop
                # we decrese the count of the leftmost element and 
                # slide window from left 
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res

        
