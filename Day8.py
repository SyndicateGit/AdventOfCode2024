f = open("Day8.txt", "r")

inputs = []

for line in f:
    inputs.append([x for x in line.strip()])

print(inputs)

# Dictionary of Letter : list of coordinates
coords = {}

for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        if inputs[i][j] in coords:
            coords[inputs[i][j]].append([i,j])
        else:
            coords[inputs[i][j]] = [[i,j]]


antinodes = set()

for letter in coords:
    if letter == ".":
        continue

    coordinates = coords[letter]
    sorted(coordinates, key=lambda x: x[0])

    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            diff_row = abs(coordinates[i][0] - coordinates[j][0])
            diff_col = coordinates[i][1] - coordinates[j][1]
            if diff_col < 0:
                if coordinates[i][0] - diff_row >= 0 and len(inputs[0]) > coordinates[i][1] + diff_col >= 0:
                    antinodes.add((coordinates[i][0] - diff_row, coordinates[i][1] + diff_col))
                    #print(coordinates[i][0] - diff_row, coordinates[i][1] + diff_col)
                if coordinates[j][0] + diff_row < len(inputs) and 0 <= coordinates[j][1] - diff_col < len(inputs[0]):
                    #print(coordinates[j][0] + diff_row, coordinates[j][1] - diff_col)
                    antinodes.add((coordinates[j][0] + diff_row, coordinates[j][1] - diff_col))
            elif diff_col > 0:
                if coordinates[i][0] - diff_row >= 0 and 0 <= coordinates[i][1] + diff_col < len(inputs[0]):
                    antinodes.add((coordinates[i][0] - diff_row, coordinates[i][1] + diff_col))
                    #print(coordinates[i][0] - diff_row, coordinates[i][1] + diff_col)
                if coordinates[j][0] + diff_row < len(inputs) and len(inputs[0]) > coordinates[j][1] - diff_col >= 0:
                    antinodes.add((coordinates[j][0] + diff_row, coordinates[j][1] - diff_col))
                    #print(coordinates[j][0] + diff_row, coordinates[j][1] - diff_col)
            else:
                if coordinates[i][0] - diff_row >= 0:
                    antinodes.add((coordinates[i][0] - diff_row, coordinates[i][1]))
                    #print(coordinates[i][0] - diff_row, coordinates[i][1])
                if coordinates[j][0] + diff_row < len(inputs):
                    antinodes.add((coordinates[j][0] + diff_row, coordinates[j][1]))
                    #print(coordinates[j][0] + diff_row, coordinates[j][1])
print(antinodes)
print(len(antinodes))

for row, col in antinodes:
    inputs[row][col] = "#"

for row in inputs:
    print("".join(row))