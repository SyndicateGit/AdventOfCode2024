from Day8 import letter

f = open("Day14.txt", "r")
t = open("test.txt", "r")

inputs = []

for line in f:
    inputs.append(line.strip().split(" "))

print(inputs)

# Grid dimensions
width = 101
height = 103


# Idea: Mod by width for x and by height for y gives position even with warp around
def move_robot(x1, y1, x2, y2, steps=100):
    x = (x1 + (x2 * steps))
    y = (y1 + (y2 * steps))
    return x%width, y%height

def safety_factor(grid):
    quadrant1 = [grid[i][0:width//2] for i in range(0, height//2)]
    quadrant2 = [grid[i][width//2 + 1:] for i in range(0, height//2)]
    quadrant3 = [grid[i][0:width//2] for i in range(height//2+1, height)]
    quadrant4 = [grid[i][width//2+1:] for i in range(height//2+1, height)]

    # check for duplicates
    for i in range(len(quadrant1)):
        for j in range(len(quadrant1[i])):
            if quadrant1[i][j] > 1:
                return 0
            if quadrant2[i][j] > 1:
                return 0
            if quadrant3[i][j] > 1:
                return 0
            if quadrant4[i][j] > 1:
                return 0
    return 1

def part1():
    grid = [[0 for x in range(width)] for y in range(height)]
    for input in inputs:
        X1 = int(input[0].split("=")[1].split(",")[0])
        Y1 = int(input[0].split("=")[1].split(",")[1])
        X2 = int(input[1].split("=")[1].split(",")[0])
        Y2 = int(input[1].split("=")[1].split(",")[1])
        x, y = move_robot(X1, Y1, X2, Y2, 100)
        grid[y][x] += 1
    for i in range(10000):
        grid = [[0 for x in range(width)] for y in range(height)]
        for input in inputs:
            X1 = int(input[0].split("=")[1].split(",")[0])
            Y1 = int(input[0].split("=")[1].split(",")[1])
            X2 = int(input[1].split("=")[1].split(",")[0])
            Y2 = int(input[1].split("=")[1].split(",")[1])
            x, y = move_robot(X1, Y1, X2, Y2, i)
            grid[y][x] += 1
        print(safety_factor(grid))
        print(i)
        if safety_factor(grid) > 0:
            for row in grid:
                row = ["" if x == 0 else x for x in row]
                print(row)
            print(i)
            break


part1()
