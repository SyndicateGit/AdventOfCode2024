f = open("Day16.txt", "r")
t = open("test.txt", "r")

# Helper functions
def display(list):
    for row in list:
        print("".join(row))

def bound_check(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

inputs = []
for line in t:
    inputs.append([x for x in line.strip()])

display(inputs)

# Idea: BFS with dictionary of {location : score}
# Want minim score for end location



visited = {}

def bfs(grid):
    directions = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
    opposite_directions = {"N": "S", "E": "W", "S": "N", "W": "E"}  # Keep track of double turn

    # Find start and end positions
    start_position = None
    end_position = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start_position = (i, j)
            if grid[i][j] == "E":
                end_position = (i, j)

    queue = [(start_position, 0, "E")]  # (position, score, direction)
    visited = {}

    while queue:
        position, score, direction = queue.pop(0)
        if position in visited and visited[position] <= score:
            continue

        visited[position] = min(visited.get(position, score), score)
        x, y = position

        # Goal reached
        if position == end_position:
            continue

        for d in directions:
            new_position = (x + directions[d][0], y + directions[d][1])

            # Can't move that way
            if not bound_check(grid, new_position[0], new_position[1]) or grid[new_position[0]][new_position[1]] == "#":
                continue

            new_score = score + 1

            if d != direction:
                new_score += 1000
            if d == opposite_directions[direction]:
                new_score += 1000

            queue.append((new_position, new_score, d))

    return visited[end_position]

def part1(grid):
    return bfs(grid)

score = part1(inputs)
print(score)
