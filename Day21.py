from collections import deque

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

# Note: Need all possible paths for each input
def numeric_directions(input):
    curr = numeric_positions["A"]
    paths = [""]

    for char in input:
        col, row = numeric_positions[char]
        diff_col, diff_row = col - curr[0], row - curr[1]
        horizontal = ""
        vertical = ""

        if diff_col > 0:
            horizontal = ">" * diff_col
        elif diff_col < 0:
            horizontal = "<" * abs(diff_col)

        if diff_row > 0:
            vertical = "v" * diff_row
        elif diff_row < 0:
            vertical = "^" * abs(diff_row)

        new_paths = []
        # Check for gap and generate possible paths
        if numeric_keypad[curr[1]][curr[0] + diff_col] == " ":
            for path in paths:
                new_paths.append(path + vertical + horizontal + "A")
        elif numeric_keypad[curr[1] + diff_row][curr[0]] == " ":
            for path in paths:
                new_paths.append(path + horizontal + vertical + "A")
        else:
            for path in paths:
                new_paths.append(path + horizontal + vertical + "A")
                if horizontal + vertical != vertical + horizontal:
                    new_paths.append(path + vertical + horizontal + "A")

        paths = new_paths
        curr = (col, row)

    return paths


print(numeric_directions(inputs[4]))

def directional_directions(directions):
    new_directions = []
    curr = directional_positions["A"]
    for char in directions:
        col, row = directional_positions[char]
        diff_col, diff_row = col - curr[0], row - curr[1]
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

# print(decode(decode("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A")))
def recursive_directions(input, n):
    if n == 0:
        return input
    return recursive_directions(directional_directions(input), n - 1)

# print(len(recursive_directions(numeric_directions(inputs[0]), 2)))

def complexities(inputs):
    count1 = 0
    for input in inputs:
        numeric = int(input[:-1])
        paths = numeric_directions(input)
        min_length = float("inf")
        for path in paths:
            length = len(recursive_directions(path, 2))
            min_length = min (min_length, length)
        print(numeric, min_length)
        count1 +=  min_length * numeric
    return count1

print(complexities(inputs))

