class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        low, high, total_area = float("inf"), float("-inf"), 0

        for x, y, l in squares:
            total_area += l*l
            low = min(low, y)
            high = max(high, y+l)
        
        target_area = total_area / 2.0

        epsilon = 1e-5

        while(high - low > epsilon):
            mid = (high + low) / 2.0

            area = 0

            for x, y, l in squares:
                h = max(0, min(l, mid - y))
                area += l * h
            
            if area < target_area:
                low = mid
            else:
                high = mid
        
        return low
