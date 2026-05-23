class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # return self.brute_force(s, t)
        return self.sliding_window(s, t)
    
    def brute_force(self, s:str, t:str) -> str:
        res, resLen = "", float("infinity")

        t_freq = {}
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1
         
        # have, need = 0, len(t)
        for i in range(len(s)):
            freqmap = {}
            for j in range(i, len(s)):
                if s[j] in t_freq.keys():
                    freqmap[s[j]] = freqmap.get(s[j], 0) + 1
                # if freqmap == t_freq:
                flag = True
                for c in t_freq:
                    if t_freq[c] > freqmap.get(c, 0):
                        flag = False
                        break
                if (j - i + 1) < resLen and flag:
                    res = s[i:j+1]
                    resLen = j - i + 1
        
        return res
    
    def sliding_window(self, s:str, t:str) -> str:
        res, resLen = "", float("infinity")

        t_freq = {}
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1
        
        l = 0
        s_freq = {}

        def isvalid(s_freq, t_freq):
            """
                returns if t_freq is <= s_freq
            """
            for c in t_freq:
                if t_freq[c] > s_freq.get(c, 0):
                    return False
            return True

        for r, c in enumerate(s):
            if c in t_freq.keys():
                s_freq[c] = s_freq.get(c, 0) + 1
            
            flag = isvalid(s_freq, t_freq)
            # 
            while flag:
                if r - l + 1 < resLen:
                    res = s[l: r + 1]
                    resLen = r - l + 1
                
                
                if s[l] in s_freq.keys():
                    s_freq[s[l]] -= 1
                    if s_freq[s[l]] == 0:
                        s_freq.pop(s[l])

                # we need to find shortest possible string 
                # that is why we are decreasing the size here
                # in positive condition 
                # when the flag becomes false 
                # then we will have shortest possible string
                l+=1

                flag = isvalid(s_freq, t_freq)
            
        return res
        
        


                