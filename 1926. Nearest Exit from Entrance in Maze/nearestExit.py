class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(maze)
        n = len(maze[0])

        def is_valid_pos(row: int, col: int):
            return 0 <= row < m and 0 <= col < n and maze[row][col] == "."

        queue = deque([(entrance[0], entrance[1], 0)])
        seen = {(entrance[0], entrance[1])}

        while queue:
            row, col, steps = queue.popleft()

            if (row, col) != (entrance[0], entrance[1]) and (row == 0 or row == m -1 or col == 0 or col == n - 1):
                return steps

            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy

                if is_valid_pos(new_row, new_col) and (new_row, new_col) not in seen:
                    queue.append((new_row, new_col, steps + 1))
                    seen.add((new_row, new_col))

        return -1