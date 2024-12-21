f = open("Day21.txt", "r")
t = open("test.txt", "r")

# Helper functions
def display(list):
    for row in list:
        print("".join(row))

def bound_check(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

inputs = []
for line in t:
    inputs.append(line.strip())

numeric_keypad = [["7", "8", "9"],
                  ["4", "5", "6"],
                  ["1", "2", "3"],
                  [" ", "0", "A"]]

numeric_positions = {char: (x, y) for y, row in enumerate(numeric_keypad) for x, char in enumerate(row)}

directional_keypad = [[" ", "^", "A"],
                      ["<", "v", ">"]]

directional_positions = {char: (x, y) for y, row in enumerate(directional_keypad) for x, char in enumerate(row)}

# Part 1
# directional -> directional -> directional -> numeric
# Part 2 likely has recursion involved with more directional layers

# Function to find path of numeric keypad given code
# Function to find path of directional keypad given code
# Recursively call function to find path of directional keypad given code with the code generated as new input

# Note: For directional keypad, up and right are the shortest distance from A. Prioritize those directions first.
def numeric_directions(input):
    curr = numeric_positions["A"]
    directions = []
    for char in input:
        col, row = numeric_positions[char]
        diff_col, diff_row = col - curr[0], row - curr[1]
        if diff_row < 0:
            directions.append("^" * abs(diff_row))
        if diff_col > 0:
            directions.append(">" * abs(diff_col))
        if diff_row > 0:
            directions.append("v" * abs(diff_row))
        if diff_col < 0:
            directions.append("<" * abs(diff_col))
        directions.append("A")
        curr = (col, row)
    return "".join(directions)

print(numeric_directions(inputs[4]))

def directional_directions(directions):
    new_directions = []
    curr = directional_positions["A"]
    for char in directions:
        col, row = directional_positions[char]
        diff_col, diff_row = col - curr[0], row - curr[1]
        if char == directional_keypad[curr[1]][curr[0]]:
            new_directions.append(char)
            continue
        if char == "<":
            if diff_row > 0:
                new_directions.append("v" * abs(diff_row))
            if diff_col < 0:
                new_directions.append("<" * abs(diff_col))
        else:
            if diff_col < 0:
                new_directions.append("<" * abs(diff_col))
            if diff_row > 0:
                new_directions.append("v" * abs(diff_row))
        if directional_keypad[curr[1]][curr[0]] == "<":
            if diff_col > 0:
                new_directions.append(">" * abs(diff_col))
            if diff_row < 0:
                new_directions.append("^" * abs(diff_row))
        else:
            if diff_row < 0:
                new_directions.append("^" * abs(diff_row))
            if diff_col > 0:
                new_directions.append(">" * abs(diff_col))

        new_directions.append("A")
        curr = (col, row)
    return  "".join(new_directions)

def decode(input):
    curr = directional_positions["A"]
    directions = []
    for char in input:
        if char == "A":
            directions.append(directional_keypad[curr[1]][curr[0]])
        elif char == "^":
            curr = (curr[0], curr[1] - 1)
        elif char == "v":
            curr = (curr[0], curr[1] + 1)
        elif char == "<":
            curr = (curr[0] - 1, curr[1])
        elif char == ">":
            curr = (curr[0] + 1, curr[1])
    return "".join(directions)

print(directional_directions(numeric_directions(inputs[3])))
print(decode(decode("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A")))
def recursive_directions(input, n):
    if n == 0:
        return input
    return recursive_directions(directional_directions(input), n - 1)

# print(len(recursive_directions(numeric_directions(inputs[0]), 2)))

def complexities(inputs):
    count = 0
    for input in inputs:
        numeric = int(input[:-1])
        length = len(recursive_directions(numeric_directions(input), 2))
        print(numeric, length)
        count +=  length * numeric
    return count

print(complexities(inputs))

