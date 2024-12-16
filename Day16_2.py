from turtledemo.penrose import start

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

grid = inputs
display(inputs)

# Idea: BFS with dictionary of {location : score}
# Want minim score for end location



visited = {}
# Find start and end positions
start_position = None
end_position = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start_position = (i, j)
        if grid[i][j] == "E":
            end_position = (i, j)

directions = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
opposite_directions = {"N": "S", "E": "W", "S": "N", "W": "E"}  # Keep track of double turn

def bfs(grid):
    queue = [(start_position, 0, "E")]  # (position, score, direction)
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

    if end_position in visited:
        return visited[end_position]
    return float("inf")

def part1(grid):
    return bfs(grid)

score = part1(inputs)
print(score)
# From visited, find minimum path
# Start at end position work backwards
def part2(grid):
    paths = set()
    paths.add(end_position)
    queue = [end_position]
    while queue:
        position = queue.pop(0)
        x, y = position

        if position == start_position:
            break

        curr_path_score = float("inf")
        min_path = []
        for d in directions:
            new_position = (x + directions[d][0], y + directions[d][1])

            if not bound_check(grid, new_position[0], new_position[1]) or grid[new_position[0]][new_position[1]] == "#":
                continue

            if new_position not in visited:
                continue

            new_path_score = visited[new_position]

            if new_path_score < curr_path_score:
                curr_path_score = new_path_score
                min_path = [new_position]

            if new_path_score == curr_path_score and new_position not in min_path:
                min_path.append(new_position)

        for path in min_path:
            paths.add(path)
        queue.extend(min_path)
    return paths

paths = part2(inputs)
new_paths = set()

# Block off path and check if new path is found with same score
for path in paths:
    x, y = path

    if path == start_position or path == end_position:
        continue

    grid[x][y] = "#"
    visited = {}
    cost = part1(grid)
    if cost == score:
        new_paths.update(part2(grid))
    grid[x][y] = "."
paths.update(new_paths)
for path in paths:
    x, y = path
    grid[x][y] = "O"
display(grid)
print(len(paths))
