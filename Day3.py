file = open("Day3.txt", "r")

inputs = ""

for line in file:
    inputs += line

list_muls = []

indexes_of_mul = []

cur_ind = 0

while cur_ind < len(inputs):
    cur_ind = inputs.find("mul", cur_ind)
    if cur_ind == -1:
        break
    indexes_of_mul.append(cur_ind)
    cur_ind += 1


def valid_mul(index):
    if index >= len(inputs) - 8:
        return 0

    mul = inputs[index:index + 3]
    if mul != "mul":
        return 0

    if inputs[index + 3] != "(":
        return 0

    num_index = index + 4
    num = ""

    while num_index < len(inputs) and inputs[num_index].isnumeric():
        num += inputs[num_index]
        num_index += 1

    if not num:
        return 0

    if inputs[num_index] != ",":
        return 0
    num_index += 1

    num2 = ""
    while num_index < len(inputs) and inputs[num_index].isnumeric():
        num2 += inputs[num_index]
        num_index += 1

    if not num2:
        return 0

    if inputs[num_index] != ")":
        return 0

    return int(num) * int(num2)



total_sum = 0
for index in indexes_of_mul:
    total_sum += valid_mul(index)

print(total_sum)
