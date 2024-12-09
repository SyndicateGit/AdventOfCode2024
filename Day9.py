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
# compact

end = len(disk) - 1
beg = 0
while beg < end:
    if beg >= len(disk) or end < 0:
        break
    while beg < end and beg < len(disk) and disk[beg] != ".":
        beg += 1
    while end > beg and end >= 0 and disk[end] == ".":
        end -= 1
    if beg < end:
        num = disk[end]
        disk[beg] = num
        disk[end] = "."
        beg += 1
        end -= 1

print(disk)
output = 0
for i in range(len(disk)):
    if disk[i] == ".":
        break
    output += disk[i]*i

print(output)