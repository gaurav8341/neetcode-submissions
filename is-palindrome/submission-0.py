class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.replace(" ", "")
        s_clean = [c.lower() for c in s if c.isalnum()]
        # print(s_clean)
        i = 0
        j = len(s_clean) - 1
        
        while i<=j:
            if s_clean[i].lower() != s_clean[j].lower():
                return False
            i += 1
            j -= 1
        
        return True