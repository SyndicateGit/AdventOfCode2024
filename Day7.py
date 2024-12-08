file = open("Day7.txt", "r")

inputs = []

for line in file:
    test = line.strip().split(" ")
    inputs.append([int(test[0][:-1])])
    inputs[-1].extend([int(x) for x in test[1:]])

print(inputs)

def check_test(numbers, total, index, curr):
    if index == len(numbers):
        if curr == total:
            return True
        return False
    if check_test(numbers, total, index + 1, curr + numbers[index]) or check_test(numbers, total, index + 1, curr * numbers[index]):
        return True

sum = 0
for test in inputs:
    total = test[0]
    numbers = test[1:]
    if check_test(numbers, total, 1, numbers[0]):
        sum += total

print(sum)