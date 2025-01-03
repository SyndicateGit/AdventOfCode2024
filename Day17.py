f = open("Day17.txt", "r")
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

registers = []
# Get registers initial values
for i in range(3):
    num = int("".join(inputs[i]).split(" ")[2])
    registers.append(num)

# Get program
program = [int(x) for x in inputs[4] if x.isdigit()]

def combo_operand(operand):
    if operand == 4:
        return registers[0] # A
    if operand == 5:
        return registers[1] # B
    if operand == 6:
        return registers[2] # C
    else:
        return operand

output = []
def run_instruction(opcode, operand, i):
    if opcode == 0: # adv
        numerator = registers[0]
        denominator = 2**combo_operand(operand)
        registers[0] = numerator // denominator
    elif opcode == 1: # bxl
        num = registers[1]
        registers[1] = num ^ operand
    elif opcode == 2: # bst
        num = combo_operand(operand)
        registers[1] = num%8
    elif opcode == 3: # jnz
        if registers[0] != 0:
            return operand # Jump to operand
    elif opcode == 4: # bxc
        registers[1] = registers[1] ^ registers[2]
    elif opcode == 5: # out
        output.append(str(combo_operand(operand)%8) + ",")
    elif opcode == 6: # bdv
        numerator = registers[0]
        denominator = 2 ** combo_operand(operand)
        registers[1] = numerator // denominator
    elif opcode == 7: # cdv
        numerator = registers[0]
        denominator = 2 ** combo_operand(operand)
        registers[2] = numerator // denominator
    return i + 2 # Move to next instruction

def run_program(program):
    i = 0
    while i < len(program):
        opcode = program[i]
        operand = program[i+1]
        i = run_instruction(opcode, operand, i)
    print("".join(output))
    return

run_program(program)