f = open("Day10.txt", "r")

inputs = []

for line in f:
    inputs.append([int(x) for x in line.strip()])

print(inputs)




# Idea: For each zero, backtrack sum_reach_9() here each time 9 is reached add index to the set.
# len(set) is the sum of 9s for that particular zero --> add to answer
zeroes = []
for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        if inputs[i][j] == 0:
            zeroes.append((i, j))

ans = 0
visited = []

def backtrack(row, col):
    if row < 0 or row >= len(inputs) or col < 0 or col >= len(inputs[0]):
        return
    if inputs[row][col] == 9:
        visited.append((row, col))
        return
    else:
        num = inputs[row][col]
        if row < len(inputs)-1 and inputs[row + 1][col] == num + 1:
            backtrack(row + 1, col)
        if row > 0 and inputs[row - 1][col] == num + 1:
            backtrack(row - 1, col)
        if col < len(inputs[0])-1 and inputs[row][col + 1] == num + 1:
            backtrack(row, col + 1)
        if col > 0 and inputs[row][col - 1] == num + 1:
            backtrack(row, col - 1)

for row, col in zeroes:
    num_nines = 0
    visited = []
    backtrack(row, col)
    ans += len(visited)

print(ans)


