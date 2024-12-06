file = open("Day6.txt", "r")
test = open("Day6_test.txt", "r")

grid = []
for line in file:
    grid.append([x for x in line.strip()])

def find_guard(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^" or grid[i][j] == "v" or grid[i][j] == "<" or grid[i][j] == ">":
                return [i,j]

guard = find_guard(grid)

# Dictionary of [translate, and next direction] given current direction
directions = {"^":[[-1,0], ">"], ">":[[0, 1], "v"], "v":[[1,0], "<"], "<":[[0,-1], "^"]}


def loop(guard, grid_copy):
    seen = {}
    while guard[0] >= 0 and guard[0] < len(grid_copy) and guard[1] >= 0 and guard[1] < len(grid_copy[0]):
        prev = guard
        direction = grid_copy[guard[0]][guard[1]]

        if (tuple(prev), direction) in seen:
            return True
        seen[(tuple(prev), direction)] = 0

        next = [prev[0] + directions[direction][0][0], prev[1] + directions[direction][0][1]]

        if next[0] < 0 or next[0] >= len(grid_copy) or next[1] < 0 or next[1] >= len(grid_copy[0]):
            break

        if grid_copy[next[0]][next[1]] == "#":
            grid_copy[prev[0]][prev[1]] = directions[direction][1]
        else:
            grid_copy[prev[0]][prev[1]] = "X"
            grid_copy[next[0]][next[1]] = direction
            guard = next
    # Not in loop
    return False

count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid_copy = []
        for row in grid:
            grid_copy.append(row.copy())
        guard = find_guard(grid_copy)
        if guard == [i,j]:
            continue
        grid_copy[i][j] = "#"
        if loop(guard, grid_copy):
            count += 1
    print(count)
print(count)
