class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # max_digonal
        res = 0
        max_d = 0
        for l, w in dimensions:
            d = (l ** 2 + w ** 2)
            # print(d, max_d)
            if d >= max_d:
            #     res = l * w
            # elif d == max_d:
                res = max(res, l * w) if d == max_d else l * w
                # res = l * w
                max_d = d#max(d, max_d)
        return res