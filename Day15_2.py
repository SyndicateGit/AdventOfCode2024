from Day8 import letter

f = open("Day15.txt", "r")
t = open("test.txt", "r")

inputs = []

def display(inputs):
    for row in inputs:
        print("".join(row))

for line in f:
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
def can_box_move(grid, box, dir, move_list=set()):
    row, col = box
    dr, dc = direction[dir]
    above = grid[row + dr][col + dc]
    if (row, col) not in move_list:
        if grid[row][col] == "[":
            move_list.add((row, col))
        else:
            move_list.add((row, col - 1))
    if above == "#":
        return False
    if above == ".": # Box can move
        return True

    if above == "[" or above == "]":
        if dir == "^" or dir == "v":
            if above == grid[box[0]][box[1]]: # Consecutive box aligns, acts like part 1
                if above == "[":
                    move_list.add((row + dr, col + dc))
                    return can_box_move(grid, (row + dr, col + dc), dir) and can_box_move(grid, (row + dr, col + 1), dir)
                else:
                    move_list.add((row + dr, col - 1))
                    return can_box_move(grid, (row + dr, col - 1), dir) and can_box_move(grid, (row + dr, col + dc), dir)

            if above == "[":
                if dir == "^":
                    move_list.add((row + dr, col + dc))
                    move_list.add((row + dr, col + 1))
                    return can_box_move(grid, (row + dr, col + dc), dir) and can_box_move(grid, (row + dr, col + 1), dir)
                if dir == "v":
                    move_list.add((row + dr, col + dc))
                    move_list.add((row + dr, col + 1))
                    return can_box_move(grid, (row + dr, col + dc), dir) and can_box_move(grid, (row + dr, col + 1), dir)
            elif above == "]":
                if dir == "^":
                    move_list.add((row + dr, col + dc))
                    move_list.add((row + dr, col - 1))
                    return can_box_move(grid, (row + dr, col + dc), dir) and can_box_move(grid, (row + dr, col - 1), dir)
                if dir == "v":
                    move_list.add((row + dr, col + dc))
                    move_list.add((row + dr, col - 1))
                    return can_box_move(grid, (row + dr, col + dc), dir) and can_box_move(grid, (row + dr, col - 1), dir)
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
        move_list = set()
        can_box_move(grid, box, dir, move_list)
        if grid[box[0]][box[1]] == "[":
            can_box_move(grid, (box[0], box[1] + 1), dir, move_list)
        else:
            can_box_move(grid, (box[0], box[1] - 1), dir, move_list)
        print(dir)
        # Replace all right of box with left of box index
        new_move_list = set()
        for box in move_list:
            if grid[box[0]][box[1]] == "]":
                new_move_list.add((box[0], box[1] - 1)) # Add left of box only
            else:
                new_move_list.add(box)
        print(new_move_list)
        # White out all boxes
        for box in move_list:
            grid[box[0]][box[1]] = "."
            grid[box[0]][box[1]+1] = "."
        # Draw boxes in new position
        for box in new_move_list:
            if grid[box[0] + dr][box[1]] == ".":
                grid[box[0] + dr][box[1]] = "["
                grid[box[0] + dr][box[1] + 1] = "]"
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
            if grid[row + dr][col + dc] == "[":
                if can_box_move(grid, (row + dr, col + dc + 1), dir):
                    grid[row][col] = "."
                    if dir == "^" or dir == "v":
                        # Need to recursively move boxes
                        prev = grid[row + dr][col + dc]
                        move_boxes(grid, (row + dr, col + dc), dir)
                        if prev == "[":
                            grid[row + dr][col + dc + 1] = "."
                        else:
                            grid[row + dr][col + dc - 1] = "."
                        grid[row + dr][col + dc] = "@"
                    else:
                        grid[row + dr][col + dc] = "@"
                        move_boxes(grid, (row + dr, col + dc), dir)
                    return (row + dr, col + dc) # updated robot position
            else:
                if can_box_move(grid, (row + dr, col + dc - 1), dir):
                    grid[row][col] = "."
                    if dir == "^" or dir == "v":
                        # Need to recursively move boxes
                        prev = grid[row + dr][col + dc]
                        move_boxes(grid, (row + dr, col + dc), dir)
                        if prev == "[":
                            grid[row + dr][col + dc + 1] = "."
                        else:
                            grid[row + dr][col + dc - 1] = "."
                        grid[row + dr][col + dc] = "@"
                    else:
                        grid[row + dr][col + dc] = "@"
                        move_boxes(grid, (row + dr, col + dc), dir)
                    return (row + dr, col + dc)
        return robot

def part1(robot, grid, inputs):
    display(grid)
    for line in inputs:
        print(line)
        for c in line:
            print(c)
            robot = move(grid, robot, c)
            print(robot)

def score(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "[":
                total += 100*i + j
    return total

part1(robot, grid, inputs)
print(score(grid))