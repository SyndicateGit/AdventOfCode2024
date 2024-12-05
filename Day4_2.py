file = open("Day4.txt", "r")

grid = []

for line in file:
    row = line.strip()
    grid.append(row)

XMAS = "MAS"
ans = 0
for row in range(len(grid) - len(XMAS) + 1):
    for col in range(len(grid[row]) - len(XMAS) + 1):
        diag_str = ''.join([grid[row + i][col + i] for i in range(len(XMAS))])
        diag_str2 = ''.join([grid[row + i][col + len(XMAS) - 1 - i] for i in range(len(XMAS))])
        if diag_str2 == diag_str or diag_str2 == diag_str[::-1]:
            ans += diag_str.count(XMAS)
            ans += diag_str.count(XMAS[::-1])
print (ans)