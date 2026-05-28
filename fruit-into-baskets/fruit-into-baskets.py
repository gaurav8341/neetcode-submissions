from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # fruits_freq = Counter(fruits)

        # vals = list(fruits_freq.values())
        # vals.sort()

        # return vals[-1]+vals[-2]

        # for _, value in fruits_freq.items():
        #     if key

        # baskets = [0, 0]

        # find longest subarray with exactly 2 unique elements
        # l = 0
        # res = 0
        # _type = set()
        # _type.add(fruits[l])

        # for r in range(1, len(fruits)):
        #     print(r, l, _type, res, fruits[l:r+1])
        #     if fruits[r] in _type:
        #         # good
        #         pass
        #     else:
        #         # check len of set of its two then remove the left most element
        #         # increment left
        #         while len(_type) >= 2:
        #             _type.remove(fruits[l])
        #             l += 1
        #             _type.add(fruits[l])
        #         # else:
        #         _type.add(fruits[r])
        #     print(r, l, r-l+1, _type)
        #     res = max(res, r - l + 1)
        # return res

        l = 0
        res = 0
        fruit_count = defaultdict(int)

        for r in range(len(fruits)):
            fruit_count[fruits[r]] += 1

            while len(fruit_count) > 2:
                fruit_count[fruits[l]] -= 1
                if fruit_count[fruits[l]] == 0:
                    del fruit_count[fruits[l]]
                l+=1

            res = max(res, r - l + 1)
        
        return res
