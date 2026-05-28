class Solution:
    def kthCharacter(self, k: int) -> str:
        # word = 'a'

        # while True:
        #     if len(word) >= k:
        #         return word[k-1]
        #     anti_word = ''
        #     for c in word:
        #         a_c = (ord(c) + 1) % 97
        #         # 97 is ascii value of a
        #         anti_word += chr(a_c + 97)
        #     word += anti_word

        # in every iteration the sring is doubled. 
        # so 2^0 == 1 when the word == 'a' a+1 = 
        # 2^1 = 2 when word  == 'ab' and so on.
        # we need to foind how many times these operation happens 


        ##I still dont understand it fully

        # Each operation effectively adds the count of 1s in the binary representation of (k - 1) to the starting character 'a'
        # The number of operations needed corresponds to the number of bits in (k - 1)'s binary representation
        # Each '1' bit represents a character increment at that operation level


        """
        Correct! Fork=8, k−1=7
        k−1=7 which is 111
        111 in binary (three 1s), so the output is 'a' + 3 shifts = 'd'. \U0001f604
        """
        return chr(ord('a') + (k - 1).bit_count())

