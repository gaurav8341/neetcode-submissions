class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # we can turn at most once 
        # we either go left and turn back right 
        # or we go right turn back left
        # in both cases total steps cant be greater than k

        # (startpos - left) + (right - left)  # left then right
        # (right - startpos) + (right -left)  # right then left 
        left, total, res = 0, 0, 0 
        for right in range(len(fruits)):
            total += fruits[right][1]
            while left <= right and min(
                abs(startPos - fruits[left][0]) + fruits[right][0] - fruits[left][0],
                abs(startPos - fruits[right][0]) + fruits[right][0] - fruits[left][0]
            ) > k:
                # right position out side of ksteps
                total -= fruits[left][1]
                left += 1
            res = max(res, total)
        return res