class Solution:
    def getMinArea(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        top = ROWS
        bottom = 0
        left = COLS
        right = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)
        
        return (bottom - top + 1) * (right - left + 1)
    
    def rotate(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])

        return [[grid[i][j] for i in range(ROWS - 1, -1, -1)] for j in range(COLS)]

    def minimumSum(self, grid: List[List[int]]) -> int:
        # find minimum area spanning 3 rects covering all ones
        # how
        #   find dist between ones 
        # cover using one rectangle
        # split that in a way where area is min
        # between 2 rect slpit the one with largest size 

        ## after reading intution
        # enumerate ways of partitioning grid along 3 parts all rect
        # for each subgrid get the area of rect covering all ones in the subgrid
        # 

        # how do i partitiion grids in 3 parts
        res = len(grid) * len(grid[0]) + 1
        for _ in range(4):
            # everytime we will rotate the array
            ROWS, COLS = len(grid), len(grid[0])
            for i in range(1, ROWS):
                # part1  would be all the rows from 0 to i 
                area1 = self.getMinArea(grid[:i])

                for j in range(1, COLS):
                    part2 = [row[:j] for row in grid[i:]]
                    part3 = [row[j:] for row in grid[i:]]
                    area2 = self.getMinArea(part2)
                    area3 = self.getMinArea(part3)

                    res = min(res, area1 + area2 + area3)

                for i2 in range(i+1, ROWS):
                    part2 = grid[i:i2]
                    part3 = grid[i2:]

                    area2 = self.getMinArea(part2)
                    area3 = self.getMinArea(part3)

                    res = min(res, area1 + area2 + area3)
            grid = self.rotate(grid)
        
        return res
            




        
