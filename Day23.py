from itertools import combinations
t = open("test.txt", "r")

# Helper functions
def display(list):
    for row in list:
        print("".join(row))

def bound_check(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def intersection(lsts):
    output = set()
    for lst in lsts:
        if len(output) == 0:
            output = set(lst)
        else:
            output = output.intersection(set(lst))
    return output

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

def find_subsets_of_three():
    subsets = set()
    for a in connections:
        for b in connections[a]:
            if b > a:
                for c in connections[b]:
                    if c > b and c in connections[a]:
                        subsets.add(tuple(sorted([a, b, c])))
    return subsets

def valid_combo(combo):
    total_connections = []
    for i in range(len(combo)):
        total_connections.append(connections[combo[i]])
        total_connections[i].append(combo[i])

    overlap = intersection(total_connections)
    for computer in combo:
        if computer not in overlap:
            return False
    return True

def set_starts_with_t(s):
    for computer in s:
        if computer[0] == "t":
            return True
    return False

def sets_of_n(n):
    three_way = set()
    combos = find_subsets_of_three()
    for combo in combos:
        three_way.add(tuple(sorted(combo)))
    return three_way

def set_has_t_computer():
    sets_of_3 = sets_of_n(3)
    print(sets_of_3)
    count = 0
    for s in sets_of_3:
        if set_starts_with_t(s):
            count += 1

    return count

print(set_has_t_computer())
