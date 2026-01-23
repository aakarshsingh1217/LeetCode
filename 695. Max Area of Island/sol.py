class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions_arr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_valid_land(row: int, col: int):
            return 0 <= col < len(grid[0]) and 0 <= row < len(grid) and grid[row][col] == 1

        curr_max_land = 0
        seen = set()

        def dfs(row: int, col: int):
            area = 1 # Count current cell.

            for x, y in directions_arr:
                new_row, new_col = row + x, col + y

                if is_valid_land(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    area += dfs(new_row, new_col)

            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if is_valid_land(i, j) and (i, j) not in seen:
                    seen.add((i, j))
                    curr_max_land = max(curr_max_land, dfs(i, j))

        return curr_max_land