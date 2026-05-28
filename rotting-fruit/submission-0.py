from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0
        time = 0


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    # add all at the same time
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1 

        while queue and fresh > 0:
            qlen = len(queue)
            for _ in range(qlen):
                i, j = queue.popleft()
                for dr, dc in directions:
                    nr = (i+dr) if 0<=(i+dr)<rows else -1
                    nc = (j+dc) if 0<=(j+dc)<cols else -1
                    if nr != -1 and nc != -1 and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1

            time += 1
            
        return time if fresh == 0 else -1
                    

