
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        maxf = 0
        l = 0
        freq_dict = defaultdict(lambda: 0)

        for r in range(len(s)):
            freq_dict[s[r]] = freq_dict.get(s[r], 0) + 1
            maxf = max(maxf, freq_dict[s[r]])

            while r - l + 1 - maxf > k:
                # we shift left
                freq_dict[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        
        return res