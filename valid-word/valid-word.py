class Solution:
    def isValid(self, word: str) -> bool:
        # valid if it is alphanumeric
        # valid if atleat one vowel aeiou
        # valid if atleast one consonent
        # valid if len is >= 3
        if not word.isalnum():
            return False
        if len(word) < 3:
            return False
        word = word.lower()
        vowels = {'a', 'e', 'i', 'o', 'u'}
        # if not vowels.intersection(set(word))
        #     return False
        vow, con = 0, 0
        for w in word:
            if not w.isalpha():
                continue
            if w in vowels:
                vow += 1
            else:
                con += 1
        
        if not vow or not con:
            return False
        
        return True

        