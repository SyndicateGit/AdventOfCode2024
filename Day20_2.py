from Day10 import visited

f = open("Day20.txt", "r")
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
start = None
end = None

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i, j)
        elif grid[i][j] == "E":
            end = (i, j)

def solve(grid, start, end):
    queue = [(start, 0)]
    visited = {}
    while queue:
        node, steps = queue.pop(0)
        x, y = node

        if node == end:
            visited[node] = min(visited.get(node, steps), steps)
            continue

        if node in visited and visited[node] <= steps:
            continue

        visited[node] = steps

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + i, y + j

            if bound_check(grid, new_x, new_y):
                if grid[new_x][new_y] == "#":
                    continue
                else:
                    queue.append(((new_x, new_y), steps + 1))

    # Backtrack to find the optimal path
    optimal_path = []
    node = end
    while node != start:
        optimal_path.append(node)
        x, y = node
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + i, y + j
            if bound_check(grid, new_x, new_y) and (new_x, new_y) in visited and visited[(new_x, new_y)] == visited[
                node] - 1:
                node = (new_x, new_y)
                break
    return visited, visited[end], optimal_path


def step_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

visited, time1, optimal_path = solve(grid, start, end)

def cheats_coord(coords, cheat=20):
    i, j = coords
    output = set()
    for di in range(-cheat, cheat + 1):
        djmax = cheat - abs(di)
        for dj in range(-djmax, djmax + 1):
            if (i + di, j + dj) in visited:
                output.add((i + di, j + dj))
    return output

def cheats (grid, cheat=20):
    count = 0
    for path in visited:
        candidates = cheats_coord(path, cheat)
        for candidate in candidates:
            if visited[candidate] - visited[path] - step_distance(path, candidate) >= 100:
                count += 1
    return count
print(cheats(grid, 20))