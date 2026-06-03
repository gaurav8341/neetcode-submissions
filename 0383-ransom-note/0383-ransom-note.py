class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransom = Counter(ransomNote)

        for a in magazine:
            if a in ransom:
                if ransom[a] > 0:
                    ransom[a] -= 1
                if ransom[a] == 0:
                    del ransom[a]

        return False if ransom else True