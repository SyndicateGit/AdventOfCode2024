f = open("Day12.txt", "r")
t = open("test.txt", "r")

inputs = []

for line in t:
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

def sides_discount():
    return 0

def calculate_plot(i, j):
    letter = inputs[i][j]
    area = 0
    perimeter = 0

    queue = [(i,j)]

    # BFS explore and add to total area and total perimeter
    while queue:
        row, col = queue.pop(0)
        if(row, col) in visited:
            continue

        if inputs[row][col] == letter:
            area += 1
            perimeter += 4 - connecting_letters(row, col)
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
    return area * perimeter

for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        if (i, j) in visited: # Skip areas already visited
            continue
        total_price += calculate_plot(i, j)

print(total_price)