def minimumMoves(n, grid, start_x, start_y, goal_x, goal_y):
    goal = (goal_x, goal_y)

    moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
    visited = {(start_x, start_y)}
    paths = [[0, start_x, start_y]]

    while len(paths) > 0:
        new_paths = []
        for path in paths:
            value, cur_x, cur_y = path

            for move in moves:
                new_x, new_y = cur_x + move[0], cur_y + move[1]

                while 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == ".":
                    if (new_x, new_y) == goal:
                        return value + 1
                    else:
                        if (new_x, new_y) not in visited:
                            visited.add((new_x, new_y))
                            new_paths.append([value + 1, new_x, new_y])

                    new_x += move[0]
                    new_y += move[1]

        paths = new_paths.copy()

    return -1


if __name__ == '__main__':
    n = int(input().strip())

    grid = []
    for _ in range(n):
        grid_item = input().strip()
        grid.append(grid_item)

    startXStartY = input().strip().split()
    startX = int(startXStartY[0])
    startY = int(startXStartY[1])
    goalX = int(startXStartY[2])
    goalY = int(startXStartY[3])

    result = minimumMoves(n, grid, startX, startY, goalX, goalY)
    print(result)
