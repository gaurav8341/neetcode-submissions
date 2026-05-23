class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows, cols = len(mat), len(mat[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float("inf")

        while queue:
            i, j = queue.popleft()
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                
                
                if mat[nr][nc] > mat[i][j] + 1:
                    queue.append((nr, nc))
                    mat[nr][nc] = mat[i][j] + 1
        
        return mat