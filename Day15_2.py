from Day8 import letter

f = open("Day15.txt", "r")
t = open("test.txt", "r")

inputs = []

def display(inputs):
    for row in inputs:
        print("".join(row))

for line in t:
    inputs.append([x for x in line.strip()])

new_inputs = []
# New warehouse
for input in inputs:
    new_line = []
    for c in input:
        if c == "#":
            new_line.append("#")
            new_line.append("#")
        if c == ".":
            new_line.append(".")
            new_line.append(".")
        if c == "@":
            new_line.append("@")
            new_line.append(".")
        if c == "O":
            new_line.append("[")
            new_line.append("]")
    new_inputs.append(new_line)

# Parse grid
grid = []
i = 0
while True:
    line = new_inputs[i]
    if not line:
        break
    grid.append(line)
    i+=1

# Parse inputs
inputs = inputs[i+1:]

display(grid)
display(inputs)

# Parse robot position
robot = (0, 0)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "@":
            robot = (i, j)

direction = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

display(grid)
display(inputs)
print(robot)

# Helper function check if box can move (recursively with other boxes in same direction)
def can_box_move(grid, box, dir):
    row, col = box
    dr, dc = direction[dir]
    above = grid[row + dr][col + dc]
    if above == "#":
        return False
    if above == ".":
        return True
    if above == "[" or above == "]":
        if dir == "^" or dir == "v":
            if above == grid[box[0]][box[1]]: # Consecutive box aligns, acts like part 1
                return can_box_move(grid, (row + dr, col + dc), dir)
            if above == "[":
                if dir == "^":
                    return can_box_move(grid, (row + dr, col + dc), dir) and can_box_move(grid, (row + dr, col + dr), dir)
                if dir == "v":
                    return can_box_move(grid, (row + dr, col + dc), dir) and can_box_move(grid, (row + dr, col - dr), dir)
        else:
            if above != grid[box[0]][box[1]]: # Consecutive box aligns, acts like part 1
                return can_box_move(grid, (row + dr, col + dc), dir)

def move_boxes(grid, box, dir):
    row, col = box
    dr, dc = direction[dir]
    if dir == "<" or dir == ">":
        # Go dr until "." then replace with "[]"
        ind = 1
        while grid[row + dr][col + dc*ind] != ".":
            ind += 1

        for i in range(1, ind):
            if grid[row + dr][col + dc * i] == "[":
                grid[row + dr][col + dc * i] = "]"
            else:
                grid[row + dr][col + dc * i] = "["

        if dir == "<":
            grid[row + dr][col + dc*ind] = "["
        else:
            grid[row + dr][col + dc*ind] = "]"
        return
    else:
        # Recursively move boxes in up or down.
        # Check if single collision or double box collision
        # If single collision, move box
        # If double box collision, move both boxes recursively by doing check again

        return

def move(grid, robot, dir):
    row, col = robot
    dr, dc = direction[dir]

    if grid[row + dr][col + dc] == "#": # Robot hit wall
        return robot

    if grid[row + dr][col + dc] == ".": # Robot moves to empty space
        grid[row][col] = "."
        grid[row + dr][col + dc] = "@"
        return (row + dr, col + dc)

    if grid[row + dr][col + dc] == "[" or grid[row + dr][col + dc] == "]": # Robot tries to move box
        # Needs to recursively check if box can move
        if can_box_move(grid, (row + dr, col + dc), dir):
            grid[row][col] = "."
            if dir == "^" or dir == "v":
                grid[row + dr][col + dc] = "@"
                # Need to recursively move boxes
                move_boxes(grid, (row + dr, col + dc), dir)
            else:
                grid[row + dr][col + dc] = "@"
                move_boxes(grid, (row + dr, col + dc), dir)
            return (row + dr, col + dc) # updated robot position

def part1(robot, grid, inputs):
    display(grid)
    print(robot)
    for line in inputs:
        print(line)
        for c in line:
            print(c)
            robot = move(grid, robot, c)
            display(grid)
            print(robot)

def score(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "0":
                total += 100*i + j
    return total

part1(robot, grid, inputs)