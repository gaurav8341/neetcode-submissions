class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # given int n 
        # we reorder the digits in n in any order such that first digit is not 0
        # return true if any no formed is power of 2

        # if n <= 2:
        #     return True

        # _set = set()

        # n_str = [s for s in str(n)]
        # # for  n_1 in n_str:
        # def permute(idx):
        #     if idx == len(n_str):
        #         if int(n_str[-1]) % 2 == 0:
        #             _set.add(int("".join(n_str)))
        #         return

        #     for i in range(len(n_str)):
        #         if idx == 0 and n_str[i] == '0':
        #             continue
        #         n_str[i], n_str[idx] = n_str[idx], n_str[i] 
        #         permute(idx + 1)
        #         n_str[idx], n_str[i] = n_str[i], n_str[idx]
            
        # permute(0)
        # # we got all the numbers of n


        # for _n in _set:
        #     while _n % 2 == 0:
        #         _n = _n // 2
        #     if _n == 1: return True
        # return False
        # n_str = str(n)
        def sort_digits(x):
            return ''.join(sorted(str(x)))
        
        target = sort_digits(n)

        for i in range(31):
            if target == sort_digits(1 << i):
                return True
        return False