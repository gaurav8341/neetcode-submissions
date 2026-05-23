class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # here 0 can be at border or surrounded by X
        # we write adfs which operates on only O and changes them to # 
        # later on we change the remaining O to X and # to O

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or 
                r >=ROWS or c >= COLS or
                board[r][c] != 'O'# only operate on 0
                ):
                return
            board[r][c]='#'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)

        for c in range(COLS):
            dfs(0, c) 
            dfs(ROWS-1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if  board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'
         

        