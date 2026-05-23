class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        count = 0
        for f in fruits:
            for idx, b in enumerate(baskets):
                # print(fruits, baskets, i, j)
                if f <= b:
                    count += 1
                    baskets[idx] = 0
                    break
        
        return n - count