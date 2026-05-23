class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # n 
        #  powers array min numbers of power of 2 that sum to n
        # @ queries [l, r]: find product of all powers from l to r
        # return do modulo 10^9 + 7
        # get product array using n

        # n_b = list(bin(n)[:1:-1]) # remove initial '0b' and reverse it ceil(log(n))
        prefix = []
        MOD = 10**9 + 7
        # for i, _b in enumerate(n_b):
        #     if _b == '1':
        #         if prefix:
        #             prefix.append(prefix[-1] * (1<< i))
        #         else:
        #             prefix.append(1<<i)
        # n_b = []
        i = 0
        while n > 0:
            if n % 2 == 1:
                if prefix:
                    prefix.append(prefix[-1] * (1<< i))
                else:
                    prefix.append(1<<i)
            n = n//2
            i += 1
        
        res = []
        for l, r in queries:
            den = 1
            if l > 0:
                den = prefix[l-1]
            # ans = int((prefix[r]/den) % (10**9 + 7))
            res.append( int((prefix[r]/den) % MOD))
        return res