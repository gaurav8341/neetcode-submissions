class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Queens canyt be placed on main central diagonals 
        # No two queens can be on same column or row
        # How to make sure queens are not on same digonals

        # negative digonal is digonal where 
        # r - c is constant across all digonal
        # positive digonal r+c is constant across all digonal

        col = set()
        negDig, posDig = set(), set()
        board = [['.'] * n for i in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                # all queens are assigned 
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or r+c in posDig or r-c in negDig:
                    continue
                
                col.add(c)
                negDig.add(r-c)
                posDig.add(r+c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posDig.remove(r + c)
                negDig.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res

