class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        # Directions ordered for easy clockwise turn calculation
        DIRECTIONS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        memo = {}

        # A clearer way to define the expected sequence based on path LENGTH
        def get_expected_value(length: int) -> int:
            if length == 1:
                return 1
            # If length is even (2, 4, 6...), value is 2
            if length % 2 == 0:
                return 2
            # If length is odd and > 1 (3, 5, 7...), value is 0
            return 0

        # DFS now returns the MAX ADDITIONAL LENGTH from (r, c) onwards
        def dfs(r: int, c: int, turns_made: int, length: int, last_dir: tuple) -> int:
            # 1. Base Case: If the current cell is invalid, this path ends. It adds 0 length.
            if not (0 <= r < ROWS and 0 <= c < COLS) or grid[r][c] != get_expected_value(length):
                return 0

            # 2. Memoization: Key is valid because the subproblem is now self-contained.
            state = (r, c, turns_made, last_dir)
            if state in memo:
                return memo[state]

            max_additional_len = 0
            next_length = length + 1
            
            # 3. Explore neighbors
            for i, current_dir in enumerate(DIRECTIONS):
                next_r, next_c = r + current_dir[0], c + current_dir[1]

                # Case A: Continue straight
                if current_dir == last_dir:
                    res = dfs(next_r, next_c, turns_made, next_length, current_dir)
                    max_additional_len = max(max_additional_len, res)

                # Case B: Make a 90-degree clockwise turn (if allowed)
                elif turns_made == 0:
                    last_dir_index = DIRECTIONS.index(last_dir)
                    if i == (last_dir_index + 1) % 4: # Check for clockwise turn
                        res = dfs(next_r, next_c, 1, next_length, current_dir)
                        max_additional_len = max(max_additional_len, res)

            # The result is 1 (for the current cell) + the best path from its neighbors
            result = 1 + max_additional_len
            memo[state] = result
            return result

        max_diagonal = 0
        has_one = False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    has_one = True
                    # A '1' by itself is a path of length 1.
                    # Start DFS from all 4 neighbors of the '1'.
                    # The path starts with length 2 at the neighbor.
                    for dr, dc in DIRECTIONS:
                        additional_len = dfs(r + dr, c + dc, 0, 2, (dr, dc))
                        max_diagonal = max(max_diagonal, 1 + additional_len)
        
        # Handle cases where the longest path is just a single '1'
        if has_one and max_diagonal == 0:
            return 1
            
        return max_diagonal