from functools import cache
from itertools import combinations
t = open("test.txt", "r")

# Helper functions
def display(list):
    for row in list:
        print("".join(row))

def bound_check(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


inputs = []
for line in t:
    inputs.append(line.strip().split("-"))

print(inputs)

connections = {}
computers = set()
for pair in inputs:
    a, b = pair
    if a not in connections:
        connections[a] = []
    if b not in connections:
        connections[b] = []
    connections[a].append(b)
    connections[b].append(a)
    computers.add(a)
    computers.add(b)

print(connections)

len_connections = {}
for computer in computers:
    len_connections[computer] = len(connections[computer])

print(len_connections)

def find_subsets_of_n(n):
    subsets = set()

    for computer in connections:
        for combo in combinations(connections[computer], n):
            # Check combinations of connections if they are all connected
            all_connected = True
            for comp in combo:
                for connection in combo:
                    if comp != connection and connection not in connections[comp]:
                        all_connected = False
                        break
                if not all_connected:
                    break
            if all_connected:
                subsets.add(tuple(sorted(combo + (computer,))))

    return sorted(subsets)

# Test out increasing n until only one subset is found
print(",".join(find_subsets_of_n(12)[0]))
