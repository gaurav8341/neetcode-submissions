class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # ROWS, COLS = len(board), len(board[0])
        ROWS_set = [set() for _ in range(9)]
        COLS_set = [set() for _ in range(9)]
        box_set = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                # check if rowset has this values
                val = board[i][j]
                if val == '.':
                    continue
                if val in ROWS_set[i]:
                    return False
                if val in COLS_set[j]:
                    return False
                

                row = i // 3
                col = j // 3
                # if i < 3:
                #     row = 0
                # elif i < 6:
                #     row = 1
                # else:
                #     row = 2
                
                # if j < 3:
                #     col = 0
                # elif j < 6:
                #     col = 1
                # else:
                #     col = 2

                if val in box_set[row][col]:
                    return False
                
                ROWS_set[i].add(val)
                COLS_set[j].add(val)
                box_set[row][col].add(val)
        
        return True