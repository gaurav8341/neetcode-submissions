class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            Dynamic sliding window problem.
            i, j right and left indexes of window.
            when character is repeated we remove all older characters
            and increament the windows
        """
        charset = set()
        max_len = 0
        i, j = 0, 0
        # i is right index of string, j in left index of string
        for i, c in enumerate(s):
            while c in charset:
                charset.remove(s[j])
                j = j + 1
            charset.add(c)
            max_len = max(max_len, i - j + 1)

        return max_len