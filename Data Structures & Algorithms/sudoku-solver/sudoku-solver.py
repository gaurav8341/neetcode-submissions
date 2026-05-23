class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [[0]*10 for _ in range(9)]
        cols = [[0]*10 for _ in range(9)]
        boxes = [[[0]*10 for _ in range(3)] for _ in range(3)]
        empty_spaces = list()

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    empty_spaces.append((i, j))
                    continue
                else: val = int(val)
                rows[i][val] += 1
                cols[j][val] += 1
                boxes[i//3][j//3][val] += 1

        def isValid(row, col, c):
            nonlocal rows, cols, boxes
            if rows[row][c]:
                return False
            if cols[col][c]:
                return False
            if boxes[row//3][col//3][c]:
                return False
            return True
        
        def set_number(r, c, val):
            nonlocal rows, cols, boxes
            rows[r][val] += 1
            cols[c][val] += 1
            boxes[r//3][c//3][val] += 1
            # rows[r].add(val)
            # cols[c].add(val)
            # boxes[r//3][c//3].add(val)
            # print(rows)
        
        def reset_number(r, c, val):
            nonlocal rows, cols, boxes
            # print(rows, r, c, val)
            rows[r][val] -= 1
            cols[c][val] -= 1
            boxes[r//3][c//3][val] -= 1
            # rows[r].remove(val)
            # cols[c].remove(val)
            # boxes[r//3][c//3].remove(val)
        
        def solve(board, idx=0):
            if idx == len(empty_spaces):
                return True

            i, j = empty_spaces[idx]
            for c in range(1, 10):
                if isValid(i, j, c):
                    set_number(i, j, c)
                    board[i][j] = str(c)
                    if solve(board, idx + 1):
                        return True
                    board[i][j] = "."
                    reset_number(i, j, c)
            return False

        solve(board, 0)