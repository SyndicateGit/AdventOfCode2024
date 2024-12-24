from functools import cache
from itertools import combinations
from logging import raiseExceptions

t = open("test.txt", "r")

# Helper functions
def display(list):
    for row in list:
        print("".join(row))

def bound_check(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


inputs = []
for line in t:
    inputs.append(line.strip())

wires = {}

input_separator = inputs.index("")

for i in range(input_separator):
    input = inputs[i]
    wire = input[:3]
    value = int(input[5:])
    wires[wire] = value

print(wires)

gates = []

for i in range(input_separator + 1, len(inputs)):
    input = inputs[i].split(" ")
    print(input)
    left = input[0]
    operator = input[1]
    right = input[2]
    output = input[-1]
    gates.append((left, right, operator, output))

print(gates)

def AND(left, right, output):
    wires[output] = wires[left] & wires[right]

def OR(left, right, output):
    wires[output] = wires[left] | wires[right]

def XOR(left, right, output):
    wires[output] = wires[left] ^ wires[right]

def gate_ready(left, right):
    return left in wires and right in wires

def process_gate(left, right, operator, output):
    if left in wires and right in wires:
        if operator == "AND":
            AND(left, right, output)
        elif operator == "OR":
            OR(left, right, output)
        elif operator == "XOR":
            XOR(left, right, output)
    else:
        raise Exception("Gate not ready")

def process_gates():
    queue = gates.copy()
    unprocessed = []
    while queue or unprocessed:
        if not queue:
            queue = unprocessed.copy()
            unprocessed = []
        gate = queue.pop(0)
        left, right, operator, output = gate
        if gate_ready(left, right):
            process_gate(left, right, operator, output)
        else:
            unprocessed.append(gate)


process_gates()

def get_z_binary():
    z_tuples = []
    for key in wires:
        if key[0] == "z":
            z_tuples.append((key, wires[key]))
    return sorted(z_tuples, key=lambda x: x[0])

z_tuples = get_z_binary()

print(z_tuples)

binary = [x[1] for x in z_tuples][::-1]
binary = "".join([str(x) for x in binary])
print(int(binary, 2))