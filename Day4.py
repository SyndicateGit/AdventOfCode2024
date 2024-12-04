file = open("Day4.txt", "r")

grid = []

for line in file:
    row = line.strip()
    grid.append(row)

XMAS = "XMAS"

ans = 0

# Check horizontally
for row in grid:
    ans += row.count(XMAS)
    ans += row.count(XMAS[::-1])

# Check vertically by rotating the grid
for col in range(len(grid[0])):
    col_str = ''.join([grid[row][col] for row in range(len(grid))])
    ans += col_str.count(XMAS)
    ans += col_str.count(XMAS[::-1])

# Check diagonally
for row in range(len(grid) - len(XMAS) + 1):
    for col in range(len(grid[row]) - len(XMAS) + 1):
        diag_str = ''.join([grid[row + i][col + i] for i in range(len(XMAS))])
        ans += diag_str.count(XMAS)
        ans += diag_str.count(XMAS[::-1])

        diag_str = ''.join([grid[row + i][col + len(XMAS) - 1 - i] for i in range(len(XMAS))])
        ans += diag_str.count(XMAS)
        ans += diag_str.count(XMAS[::-1])

print (ans)
