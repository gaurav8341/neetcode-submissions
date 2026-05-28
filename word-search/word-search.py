class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Visit map It should be reset in outer loopp
        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]


        def dfs(i, j, idx):

            if idx == len(word):
                return True

            if i < 0 or j < 0 or \
                i >= ROWS or j >= COLS or \
                board[i][j] != word[idx] or visited[i][j]:
                return False 
            
            # if len(substr) == len(word):
                # if substr[-1] == word[-1]
            # if trk_idx = len(word) - 1:
            #     # All the chars matched and now return true
            #     return True
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            visited[i][j] = True
            
            res = (dfs(i + 1, j, idx + 1) or
                    dfs(i - 1, j, idx + 1) or
                    dfs(i, j + 1, idx + 1) or
                    dfs(i, j - 1, idx + 1))
            
            visited[i][j] = False
            return res

        # visit = [[False] * len(board[0])] * len(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False