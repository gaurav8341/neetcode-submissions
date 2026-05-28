class Solution:
    
    def bfs(self, r, c):
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        queue = collections.deque([(r,c)])

        level = 0
        while queue:
            qlen = len(queue)
            for _ in range(qlen):
                i, j = queue.popleft()
                if level < self.grid[i][j]:
                    self.grid[i][j] = level

                for dr, dc in directions:
                    nr = i+dr if 0<=(i+dr)<self.rows else -1
                    nc = j+dc if 0<=(j+dc)<self.cols else -1
                    if nr != -1 and nc != -1 and self.grid[nr][nc]>0 and self.grid[nr][nc]>(level+1):
                        queue.append((nr, nc))
            level += 1

                    
        



    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 0:
                    # do bfs
                    print(i, j)
                    self.bfs(i, j)
                    print(self.grid)

        grid = self.grid

        # return self.grid
