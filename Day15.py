from Day8 import letter

f = open("Day15.txt", "r")
t = open("test.txt", "r")

inputs = []

def display(inputs):
    for row in inputs:
        print("".join(row))

for line in f:
    inputs.append([x for x in line.strip()])

# Parse grid
grid = []
i = 0
while True:
    line = inputs[i]
    if not line:
        break
    grid.append(line)
    i+=1

# Parse inputs
inputs = inputs[i+1:]

# Parse robot position
robot = (0, 0)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "@":
            robot = (i, j)

direction = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

def move(grid, robot, dir):
    col, row = robot
    dr, dc = direction[dir]

    if grid[row + dr][col + dc] == "#": # Robot hit wall
        return robot

    if grid[row + dr][col + dc] == ".": # Robot moves to empty space
        grid[row][col] = "."
        grid[row + dr][col + dc] = "@"
        return (col + dc, row + dr)

    if grid[row + dr][col + dc] == "O": # Robot tries to move box
        # Check if box can move, box tries to move in direction of robot
        boxes = 1
        # Get box in a row count
        while grid[row + dr*boxes][col + dc*boxes] == "O":
            boxes += 1
        # Check if end of boxes is empty or wall
        if grid[row + dr*boxes][col + dc*boxes] == "#": # Box hits wall
            return robot

        if grid[row + dr*boxes][col + dc*boxes] == ".": # Box moves to empty space
            grid[row][col] = "."
            grid[row + dr][col + dc] = "@"
            grid[row + dr*boxes][col + dc*boxes] = "O"
            return (col + dc, row + dr)

def part1(robot, grid, inputs):
    display(grid)
    print(robot)
    for line in inputs:
        print(line)
        for c in line:
            robot = move(grid, robot, c)
            display(grid)
            print(robot)

def score(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                total += 100*i + j
    return total

part1(robot, grid, inputs)
print(score(grid))