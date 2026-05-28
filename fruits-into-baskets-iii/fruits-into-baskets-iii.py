class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # SAME POROBLEM AS YESTERDAY
        # constrants are wider  cant have n^2 soluyion
        # segment trees basically get the sum of any segment of array in o(logn) time 

        # segment tree 
        # each leaf node is elem from baskets
        # each parent node will have max of its children

        # Segment tree size is 2 * N, where N is the nearest power of 2 ≥ n
        # checking if number is valid or not would have been easier
        n = len(baskets)
        N = 1
        while N <= n:
            N <<= 1
        # if n % 2 == 0:
        #     N += 1 # it should be power of 2
        
        segTree = [0] * (2 * N)
        
        for i in range(n):
            # in all the lead nodes will have basket elems
            segTree[N + i] = baskets[i]

        for i in range(N - 1, 0 , -1):
            # here last n elems will be baskets elems
            # We done want to consider the leaf elems in the above thing
            segTree[i] = max(segTree[2*i], segTree[2*i + 1])
        
        count = 0
        for fruit in fruits:
            idx = 1
            if segTree[idx] < fruit:
                count += 1
                continue
            
            while idx < N:
                if segTree[2 * idx] >= fruit:
                    idx *= 2# idx is doubled
                else:
                    # 
                    idx = 2 * idx + 1
            
            segTree[idx] = -1
            while idx > 1:
                idx //= 2
                segTree[idx] = max(segTree[2 * idx], segTree[2 * idx + 1])
        
        return count