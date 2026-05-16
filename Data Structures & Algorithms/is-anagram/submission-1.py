class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        s_map = {}

        if s_len != t_len:
           return False

        for ch in s:
            s_map[ch] = s_map.get(ch, 0) + 1
        
        for ch in t:
            if ch not in s_map.keys():
                return False
            
            if s_map.get(ch) > 1:
                s_map[ch] -= 1 
            else:
                s_map.pop(ch)
        
        return True

        