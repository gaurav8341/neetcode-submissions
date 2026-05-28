class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        vertices = set() # we will  store the top left and bottom right coords of square here vertices = set() # we will  store the top left and bottom right coords of square here
        # storing i, j, dist is much more better way 
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1 and i > 0 and j > 0:
                    # min left (ie i, j-1), top (ie i-1, j), and digonal (ie i-1, j-1)
                    matrix[i][j] = min(
                        matrix[i-1][j-1], 
                        matrix[i][j-1], 
                        matrix[i-1][j]) + 1
                res += matrix[i][j] 
        
        return res