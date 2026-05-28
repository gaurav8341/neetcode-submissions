class Solution:
    # self.directions = [[1,0],[0,1],[-1,0],[0,-1]]
    def dfs(self, r, c):
        if (r < 0 or r >=self.rows or c < 0 or c >= self.cols):
            return 0
        if self.grid[r][c] != 1:
            return 0
        # area += 1
        self.grid[r][c] = 0
        return (1 + self.dfs(r-1, c) + self.dfs(r+1,c) + self.dfs(r, c+1) + self.dfs(r, c-1))

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])   

        maxArea = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j]==1:
                    maxArea = max(self.dfs(i,j), maxArea)
        
        return maxArea