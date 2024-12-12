from Day8 import letter

f = open("Day12.txt", "r")
t = open("test.txt", "r")

inputs = []

for line in f:
    inputs.append([x for x in line.strip()])

# Idea: Keep track of areas visited
# If area is visited, skip
# For Area: count all connecting of same character,
# while doing that, count not connected areas for
# perimeter

total_price = 0

visited = set()

def connecting_letters(i, j):
    letter = inputs[i][j]
    connections = 0
    if i - 1 >= 0 and inputs[i-1][j] == letter:
        connections += 1
    if i + 1 < len(inputs) and inputs[i+1][j] == letter:
        connections += 1
    if j - 1 >= 0 and inputs[i][j-1] == letter:
        connections += 1
    if j + 1 < len(inputs[i]) and inputs[i][j+1] == letter:
        connections += 1
    return connections

def diagonal_connections(i, j):
    letter = inputs[i][j]
    connections = 0
    if i - 1 >= 0 and j - 1 >= 0 and inputs[i-1][j-1] == letter:
        connections += 1
    if i + 1 < len(inputs) and j + 1 < len(inputs[i]) and inputs[i+1][j+1] == letter:
        connections += 1
    if i - 1 >= 0 and j + 1 < len(inputs[i]) and inputs[i-1][j+1] == letter:
        connections += 1
    if i + 1 < len(inputs) and j - 1 >= 0 and inputs[i+1][j-1] == letter:
        connections += 1
    return connections

def diaganol_same_side(i, j):
    letter = inputs[i][j]
    if i - 1 >= 0 and j - 1 >= 0 and inputs[i - 1][j - 1] == letter:
        if i - 1 and j + 1 < len(inputs[i]) and inputs[i - 1][j + 1] == letter:
            return True
    # Downward facing diagnols connected
    if i + 1 < len(inputs) and j - 1 >= 0 and inputs[i + 1][j - 1] == letter:
        if i + 1 >= 0 and j + 1 <len(inputs) and inputs[i + 1][j + 1] == letter:
            return True
    # Left facing diagnols connected
    if i - 1 >= 0 and j - 1 >= 0 and inputs[i - 1][j - 1] == letter:
        if i + 1 < len(inputs) and j - 1 >= 0 and inputs[i + 1][j - 1] == letter:
            return True
    # Right facing diagnols connected
    if i - 1 >= 0 and j + 1 < len(inputs[i]) and inputs[i - 1][j + 1] == letter:
        if i + 1 < len(inputs) and j + 1 < len(inputs[i]) and inputs[i + 1][j + 1] == letter:
            return True
    return False

def hasNorth(i, j):
    letter = inputs[i][j]
    if i - 1 >= 0 and inputs[i - 1][j] == letter:
        return True
    return False

def hasSouth(i, j):
    letter = inputs[i][j]
    if i + 1 < len(inputs) and inputs[i + 1][j] == letter:
        return True
    return False

def hasEast(i, j):
    letter = inputs[i][j]
    if j + 1 < len(inputs[i]) and inputs[i][j + 1] == letter:
        return True
    return False

def hasWest(i, j):
    letter = inputs[i][j]
    if j - 1 >= 0 and inputs[i][j - 1] == letter:
        return True
    return False

def hasNorthEast(i, j):
    letter = inputs[i][j]
    if i - 1 >= 0 and j + 1 < len(inputs[i]) and inputs[i - 1][j + 1] == letter:
        return True
    return False

def hasNorthWest(i, j):
    letter = inputs[i][j]
    if i - 1 >= 0 and j - 1 >= 0 and inputs[i - 1][j - 1] == letter:
        return True
    return False

def hasSouthEast(i, j):
    letter = inputs[i][j]
    if i + 1 < len(inputs) and j + 1 < len(inputs[i]) and inputs[i + 1][j + 1] == letter:
        return True
    return False

def hasSouthWest(i, j):
    letter = inputs[i][j]
    if i + 1 < len(inputs) and j - 1 >= 0 and inputs[i + 1][j - 1] == letter:
        return True
    return False

def corners(current_visited):
    count = 0
    for i, j in current_visited:
        if(not hasNorth(i, j) and not hasWest(i, j)):
            count += 1
        if(not hasNorth(i, j) and not hasEast(i, j)):
            count += 1
        if(not hasSouth(i, j) and not hasWest(i, j)):
            count += 1
        if(not hasSouth(i, j) and not hasEast(i, j)):
            count += 1
        if(hasNorth(i, j) and hasWest(i, j) and not hasNorthWest(i, j)):
            count += 1
        if(hasNorth(i, j) and hasEast(i, j) and not hasNorthEast(i, j)):
            count += 1
        if(hasSouth(i, j) and hasWest(i, j) and not hasSouthWest(i, j)):
            count += 1
        if(hasSouth(i, j) and hasEast(i, j) and not hasSouthEast(i, j)):
            count += 1
    return count

def calculate_plot(i, j):
    letter = inputs[i][j]
    area = 0
    queue = [(i,j)]
    current_visited = set()
    # BFS explore and add to total area and total perimeter
    while queue:
        row, col = queue.pop(0)
        if(row, col) in visited:
            continue

        if inputs[row][col] == letter:
            area += 1
            if (connecting_letters(row, col) + diagonal_connections(row, col) < 8):
                current_visited.add((row, col))
            visited.add((row, col))
        else:
            continue

        # Explore connected areas
        if row - 1 >= 0 and (row-1, col) not in visited:
            queue.append((row-1, col))

        if row + 1 < len(inputs) and (row+1, col) not in visited:
            queue.append((row+1, col))

        if col - 1 >= 0 and (row, col-1) not in visited:
            queue.append((row, col-1))

        if col + 1 < len(inputs[row]) and (row, col+1) not in visited:
            queue.append((row, col+1))

    perimeter = corners(current_visited)
    print("Letter: ", letter, "Perimeter: ", perimeter, "Area: ", area)
    return area * perimeter

for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        if (i, j) in visited: # Skip areas already visited
            continue
        total_price += calculate_plot(i, j)

print(total_price)