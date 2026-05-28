class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # for top right to bottom left digonal elems i + j is same
        # for top left to bottom left just increament i by 1 and j by 1

        # we start at 0,0
        digonals = []

        ROWS, COLS = len(mat), len(mat[0])

        # pos = (0, 0)
        r, c = 0, 0
        up = True
        while len(digonals) < (ROWS * COLS):
            # r, c = pos
            digonals.append(mat[r][c])
            
            if (r + c) % 2 == 0:
                # up
                
                if c == COLS - 1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
                # r = r + 1 if c == COLS - 1 else r - 1
                # c = c if c == COLS - 1 else c + 1
            else:
                # down
                if r == ROWS - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
                # r = r if r == ROW - 1 else r + 1
                # c = c - 1 if r == ROW - 1 else c + 1 


        return digonals