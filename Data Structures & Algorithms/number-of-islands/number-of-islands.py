import collections
class Solution:
    # def bfs( r, c):
    #     # only go there if its land
    #     print("bfs")
    #     directions = [[-1,0], [1, 0], [0, -1], [0, 1]]
    #     queue = [] # only append if value is 1
    #     queue.append((r, c))
    #     grid[r][c] = "0"
    #     while queue:
    #         i, j = queue.pop(0)
    #         print("queue",queue)
    #         for rt, ct in directions:
    #             nr = i+rt if 0<=(i+rt)<len(grid) else None
    #             nc = j+ct if 0<=(j+ct)<len(grid[0]) else None
    #             if nr and nc and grid[nr][nc] == "1":
    #                 queue.append([nr, nc])
    #                 grid[nr][nc] = "0"
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        # i,j,c,r = 0,0, len(grid[0])-1, len(grid) - 1
        def bfs( r, c):
        # only go there if its land
            # print("bfs")
            directions = [[-1,0], [1, 0], [0, -1], [0, 1]]
            queue = collections.deque() # only append if value is 1
            queue.append((r, c))
            grid[r][c] = "0"
            while queue:
                i, j = queue.popleft()
                # print("queue",queue)
                for rt, ct in directions:
                    nr = i+rt if 0<=(i+rt)<len(grid) else -1
                    nc = j+ct if 0<=(j+ct)<len(grid[0]) else -1
                    if nr!=-1 and nc!=-1 and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        # print("hello", queue, nr, nc)

                        grid[nr][nc] = "0"
        cnt = 0
        for i in range(len(grid)):
            # rows
            for j in range(len(grid[0])):
                # print("i, j", i, j, grid[i][j])
                if grid[i][j] == "1":
                    bfs( i, j)
                    cnt += 1
                
        return cnt