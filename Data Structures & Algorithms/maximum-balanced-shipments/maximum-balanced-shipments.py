class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        # array 

        _max = 0
        cnt = 0
        for n in weight:
            if n > _max:
                _max = n
            elif n < _max:
                cnt += 1
                _max = 0
        return cnt