from collections import deque
# BFS approach


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return "please input a grid"
        num_island = 0
        row, column = len(grid), len(grid[0])
        mapped = set()

        def dfs(x_point, y_point):
            coordinates = deque()
            mapped.add((x_point, y_point))
            coordinates.append((x_point, y_point))

            while coordinates:
                # for BFS approach change 'pop' to 'popleft'
                x_point, y_point = coordinates.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dx, dy in directions:
                    row_move, colm_move = x_point + dx, y_point + dy
                    if (row_move in range(row) and
                        colm_move in range(column)
                        and grid[row_move][colm_move] == '1' and
                            (row_move, colm_move) not in mapped):
                        coordinates.append((row_move, colm_move))
                        mapped.add((row_move, colm_move))

        for x_point in range(row):
            for y_point in range(column):
                if (grid[x_point][y_point] == '1' and
                        (x_point, y_point) not in mapped):
                    dfs(x_point, y_point)
                    num_island += 1

        return num_island


grid = [
    # Should return 1 Island
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
grid_two = [
    # Should Return 3 Islands
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
solution = Solution()
print(solution.numIslands(grid_two))
