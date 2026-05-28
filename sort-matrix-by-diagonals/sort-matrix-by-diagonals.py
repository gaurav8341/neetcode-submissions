import heapq
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        # so the idea is we maintain list for diff digonals
        # if that list is heap then we can sort it at insertion only.

        # so we need dict, what will be dict the diff between i and j, i-j
        # for 0: its decreasing
        # -1: increaing
        # 1: decreaing
        # for upper triangle half its increasing wher i - j < 0
        # for lower half triangle including middle it would be decreasing: i-j >= 0

        diagonals = {} 

        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                k = i - j
                if k not in diagonals:
                    diagonals[k] = []
                if k >= 0:
                    heapq.heappush(diagonals[k], -grid[i][j])
                else:
                    heapq.heappush(diagonals[k], grid[i][j])
        
        for i in range(ROWS):
            for j in range(COLS):
                k = i - j
                grid[i][j] = heapq.heappop(diagonals[k])
                if k >= 0:
                    grid[i][j] *= -1

        return grid

