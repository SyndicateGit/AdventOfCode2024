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

count = 0
while guard[0] >= 0 and guard[0] < len(grid) and guard[1] >= 0 and guard[1] < len(grid[0]):
    prev = guard
    direction = grid[guard[0]][guard[1]]
    next = [prev[0] + directions[direction][0][0], prev[1] + directions[direction][0][1]]
    if next[0] < 0 or next[0] >= len(grid) or next[1] < 0 or next[1] >= len(grid[0]):
        break
    if grid[next[0]][next[1]] == "#":
        grid[prev[0]][prev[1]] = directions[direction][1]
    else:
        grid[prev[0]][prev[1]] = "X"
        grid[next[0]][next[1]] = direction
        guard = next

for row in grid:
    count += row.count("X")

print(count+1)
