f = open("Day18.txt", "r")
t = open("test.txt", "r")

# Helper functions
def display(list):
    for row in list:
        print("".join(row))

def bound_check(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

inputs = []
for line in t:
    inputs.append([int(x) for x in line.strip().split(",")])

bytes = []
for input in inputs:
    x = input[0]
    y = input[1]
    bytes.append((x, y))

# Default 70 by 70 grid
grid = [["." for x in range(71)] for y in range(71)]



steps = 1028
# set up first k bytes
for i in range(steps):
    x, y = bytes[i]
    print(x, y)
    grid[y][x] = "#"



# Find exit (col is largest of # and row is largest of #)
exit = (70, 70)

display(grid)

visited = {} # (x, y) -> steps
def min_steps(grid):
    queue = [(0,0,0)] # (x, y, steps)

    while queue:
        x, y, step = queue.pop(0)
        if (x, y) == exit:
            return step
        if (x, y) in visited and visited[(x, y)] <= step:
            continue
        visited[(x, y)] = step
        print(x, y, step)
        if not bound_check(grid, x, y) or grid[x][y] == "#":
            continue

        queue.append((x + 1, y, step+1))
        queue.append((x - 1, y, step+1))

        queue.append((x, y + 1, step+1))
        queue.append((x, y - 1, step+1))

    return visited[(exit[0], exit[1])] if (exit[0], exit[1]) in visited else -1

print(min_steps(grid))