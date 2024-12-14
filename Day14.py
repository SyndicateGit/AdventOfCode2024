from Day8 import letter

f = open("Day14.txt", "r")
t = open("test.txt", "r")

inputs = []

for line in t:
    inputs.append(line.strip().split(" "))

print(inputs)

# Grid dimensions
width = 11
height = 7
grid = [[0 for x in range(width)] for y in range(height)]


# Idea: Mod by width for x and by height for y gives position even with warp around
def move_robot(x1, y1, x2, y2, steps=100):
    x = (x1 + (x2 * steps))
    y = (y1 + (y2 * steps))
    return x%width, y%height

def safety_factor():
    quadrant1 = [grid[i][0:width//2] for i in range(0, height//2)]
    quadrant2 = [grid[i][width//2 + 1:] for i in range(0, height//2)]
    quadrant3 = [grid[i][0:width//2] for i in range(height//2+1, height)]
    quadrant4 = [grid[i][width//2+1:] for i in range(height//2+1, height)]

    sum1 = sum([sum(x) for x in quadrant1])
    sum2 = sum([sum(x) for x in quadrant2])
    sum3 = sum([sum(x) for x in quadrant3])
    sum4 = sum([sum(x) for x in quadrant4])

    return sum1 * sum2 * sum3 * sum4

def part1():
    grid = [[0 for x in range(width)] for y in range(height)]
    for input in inputs:
        X1 = int(input[0].split("=")[1].split(",")[0])
        Y1 = int(input[0].split("=")[1].split(",")[1])
        X2 = int(input[1].split("=")[1].split(",")[0])
        Y2 = int(input[1].split("=")[1].split(",")[1])
        x, y = move_robot(X1, Y1, X2, Y2, 100)
        grid[y][x] += 1
    print(safety_factor())

    for row in grid:
        print(row)
part1()
