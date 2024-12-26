from functools import cache
from itertools import combinations
from logging import raiseExceptions

t = open("test.txt", "r")

# Helper functions
def display(list):
    for row in list:
        print("".join(row))

def bound_check(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


inputs = []
for line in t:
    inputs.append(line.strip()) if line.strip() != "" else None

items = []

print(inputs)
for i in range(0, len(inputs), 7):
    if inputs[i] == "":
        continue
    grid = []
    for j in range(7):
        grid.append(inputs[i+j])
    items.append(grid)


# Convert item to type and heights
def get_type(item):
    num_top = item[0].count("#")
    num_bottom = item[-1].count("#")
    if num_top > num_bottom:
        return "KEY"
    else:
        return "LOCK"

def get_heights(item):
    display(item)
    heights = [0] * len(item[0])
    for i in range(len(item)):
        for j in range(len(item[0])):
            if item[i][j] == "#":
                heights[j] += 1
    print(heights)
    return heights

keys = []
locks = []
for item in items:
    if get_type(item) == "KEY":
        keys.append(get_heights(item))
    else:
        locks.append(get_heights(item))

def sort_by_height_i(items, i):
    return sorted(items, key=lambda x: x[i])

def overlap(key, lock):
    for i in range(len(key)):
        if key[i] + lock[i] > 7:
            return True
    return False

print(keys)
print(locks)

def get_no_overlaps(keys, locks):
    fits = set() # (key, lock)
    for i in range(len(keys)):
        for j in range(len(locks)):
            key = keys[i]
            lock = locks[j]
            if not overlap(key, lock):
                fits.add((tuple(key), tuple(lock)))

    return fits

print(len(get_no_overlaps(keys, locks)))
