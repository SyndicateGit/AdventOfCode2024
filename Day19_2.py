from platform import uname

f = open("Day19.txt", "r")
t = open("test.txt", "r")

# Helper functions
def display(list):
    for row in list:
        print("".join(row))

def bound_check(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

inputs = []
for line in t:
    inputs.append([x for x in line.strip().split(", ")])

towels = inputs[0]
designs = inputs[2:]
print(towels)
print(designs)
memo = {}
def possible(towels, design):
    if design in memo:
        return memo[design]

    if design in towels:
        memo[design] = True
        return True

    if len(design) == 1:
        memo[design] = False
        return False

    for i in range(1, len(design)):
        if possible(towels, design[:i]) and possible(towels, design[i:]):
            memo[design] = True
            return True

    if design not in memo:
        memo[design] = False
    return memo[design]

def combinations(towels, design):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1 # only one way to have an empty string

    for i in range(1, n + 1):
        for towel in towels:
            if i >= len(towel) and design[i - len(towel):i] == towel:
                dp[i] += dp[i - len(towel)]

    return dp[n]

count = 0
for design in designs:
    print(design)
    if possible(towels, design[0]):
        candidates = set()
        for towel in towels:
            if towel in design[0]:
                candidates.add(towel)
        count += combinations(candidates, design[0])


print(count)