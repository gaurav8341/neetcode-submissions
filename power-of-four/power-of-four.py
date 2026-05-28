import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        # while n > 1:
        #     if n % 4 == 0:
        #         n = n // 4
        #     else:
        #         return False
        # return n == 1
        
        if n <= 0: return False
        x = math.log(n, 4) # 4 as base
        return x % 1 == 0 # check if x is integer ie whole number
