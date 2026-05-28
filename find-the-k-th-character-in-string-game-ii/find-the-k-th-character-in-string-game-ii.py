class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n, i  =  1, 0 
        # n is len of string 
        while n<k:
            n *= 2
            i += 1
        
        d = 0
        while n > 1:
            if k > n // 2:
                # ks is in second half
                k = k - n//2
                # getting first half element 
                # from where kth element was derived
                d = d + operations[i-1]
            n //= 2
            i -= 1
        return chr(d%26 + ord("a"))

        # shift = 0

        # for i

        


        # return chr(ord('a') + shift)
