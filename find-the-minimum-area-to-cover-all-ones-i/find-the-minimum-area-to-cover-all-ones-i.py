class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # idea is 2 pointer approach to find the top most and bottom most point
        # same for left most right most
        # idea is to do in 2 pass
        # ROWS, COLS = len(grid), len(grid[0])
        # top, bottom = 0, len(grid) - 1
        # # idea is if we find then no incr, decr should happen for that idx
        # is_top, is_bottom = False, False 
        # while top <= bottom :#and (not found_top or not found_bottom):
        #     # i
        #     if is_top and is_bottom:
        #         break
            
        #     for j in range(COLS):
        #         if not is_top:
        #             # check all columns for 1
        #             if grid[top][j] == 1:
        #                 is_top = True
        #         if not is_bottom:
        #             if grid[bottom][j] == 1:
        #                 is_bottom = True
        #     if not is_top:
        #         top += 1
        #     if not is_bottom:
        #         bottom -= 1

        # height = bottom - top + 1

        # left, right = 0, len(grid[0]) - 1
        # # idea is if we find then no incr, decr should happen for that idx
        # is_left, is_right = False, False 
        # while left <= right :#and (not found_top or not found_bottom):
        #     # i
        #     if is_left and is_right:
        #         break
            
        #     for j in range(ROWS):
        #         if not is_left:
        #             # check all columns for 1
        #             if grid[j][left] == 1:
        #                 is_left = True
        #         if not is_right:
        #             if grid[j][right] == 1:
        #                 is_right = True
        #     if not is_left:
        #         left += 1
        #     if not is_right:
        #         right -= 1
        
        # width = right - left + 1

        # return height * width

        ROWS, COLS = len(grid), len(grid[0])
        top, bottom = ROWS, 0 
        left, right = COLS, 0 

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    # bottom = j
                    left = min(left, j)
                    right = max(right, j)
                    # right = j
        
        return (bottom - top + 1) * (right - left + 1)


        
        
            