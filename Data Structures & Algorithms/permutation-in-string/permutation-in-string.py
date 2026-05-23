class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)

        if s1_len > len(s2):
            return False
        
        s1_freq = {}
        for c in s1:
            s1_freq[c] = s1_freq.get(c, 0) + 1
        
        s2_freq = {}
        print(s1_freq)
        for i in range(len(s2)):
            s2_freq[s2[i]] = s2_freq.get(s2[i], 0) + 1
            print(s2_freq)
            if s2_freq == s1_freq:
                return True
            elif i >= s1_len - 1:
                s2_freq[s2[i-s1_len + 1]] -= 1
                if s2_freq[s2[i-s1_len + 1]] == 0:
                    s2_freq.pop(s2[i-s1_len + 1])
        
        return False

