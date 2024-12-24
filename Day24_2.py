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

def get_char_binary(char):
    z_tuples = []
    for key in wires:
        if key[0] == char:
            z_tuples.append((key, wires[key]))
    return sorted(z_tuples, key=lambda x: x[0])

z_tuples = get_char_binary("z")
x_tuples = get_char_binary("x")
y_tuples = get_char_binary("y")

print(z_tuples)
print(x_tuples)
print(y_tuples)

z_binary = [x[1] for x in z_tuples][::-1]
z_binary = "".join([str(x) for x in z_binary])
z_int = int(z_binary, 2)

x_bin = [x[1] for x in x_tuples][::-1]
x_bin = "".join([str(x) for x in x_bin])
x_int = int(x_bin, 2)

y_bin = [x[1] for x in y_tuples][::-1]
y_bin = "".join([str(x) for x in y_bin])
y_int = int(y_bin, 2)


print(x_bin)
print(y_bin)
print(z_binary)

print(x_int)
print(y_int)
print(z_int)

# Shows which bits lead to a mismatch, work each mismatch bit one by one from least significant bit
def mismatched_bits(x, y, z):
    sum_xy = int(x, 2) + int(y, 2)
    z_int = int(z, 2)
    return bin(sum_xy ^ z_int)

print(mismatched_bits(x_bin, y_bin, z_binary))

# z16 is mismatched. Check z16, x16, y16
