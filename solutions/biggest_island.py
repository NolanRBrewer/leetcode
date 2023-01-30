# find the island that covers the most area
from collections import deque


def biggest_island(grid):
    num_island = 0
    row, column = len(grid), len(grid[0])
    islands = {}
    mapped = set()
    # print(dfs)

    def dfs(x_point, y_point):
        island_area = 1
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
                    and grid[row_move][colm_move] == 1 and
                        (row_move, colm_move) not in mapped):
                    coordinates.append((row_move, colm_move))
                    mapped.add((row_move, colm_move))
                    island_area += 1
        return island_area

    for x_point in range(row):
        for y_point in range(column):
            if (grid[x_point][y_point] == 1 and
                    (x_point, y_point) not in mapped):
                islands[num_island] = dfs(x_point, y_point)
                num_island += 1

    return max(islands.values())


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

print(biggest_island(grid))
