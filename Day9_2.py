f = open("Day9.txt", "r")
t = open("test.txt", "r")

inputs = []

for line in f:
    inputs.extend([int(x) for x in line.strip()])

disk = []

# load disk with id, empty space pattern
for i in range(len(inputs)):
    if i % 2 == 0:
        for j in range(inputs[i]):
            disk.append(i//2) # ID
    else:
        for j in range(inputs[i]):
            disk.append(".")

print(disk)

count = {}
spaces = [] # index, number of spaces

for value in disk:
    if value != ".":
        if value in count:
            count[value] += 1
        else:
            count[value] = 1

print(count)

beg = 0
while beg < len(disk):
    while beg < len(disk) and disk[beg] != ".":
        beg += 1
    space = 0
    index = beg
    while beg < len(disk) and disk[beg] == ".":
        space += 1
        beg += 1
    spaces.append((index, space))
    beg += 1

print(spaces)

def enough_space(space, index):
    curr = 0
    if index >= len(disk):
        return False
    while(index < len(disk) and disk[index] == "."):
        curr += 1
        index += 1
    return curr >= space


end = len(disk) - 1

while end > 0:
    while end >= 0 and disk[end] == ".":
        end -= 1

    if end < 0:
        break

    num = disk[end]
    space_needed = count[num]
    for index, space in spaces:
        if index >= end:
            break
        if space >= space_needed:
            for i in range(space_needed):
                disk[index+i] = num
                disk[end-i] = "."
            spaces.remove((index, space))
            if space > space_needed:
                spaces.append((index+space_needed, space-space_needed))
            spaces.sort()
            break
    end -= space_needed

output = 0
for i in range(len(disk)):
    if disk[i] == ".":
        continue
    output += disk[i]*i

print(output)