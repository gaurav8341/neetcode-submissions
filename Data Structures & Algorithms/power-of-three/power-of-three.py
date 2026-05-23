class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        # while n > 1:
        #     if n % 3 == 0:
        #         n = n // 3
        #     else:
        #         return False
        
        # return n == 1
        # if n == 1: return True

        last = 1
        while last < n:
            power = last * 3
            if power == n:
                return True
            last = power
        
        return last == n