f = open("Day11.txt", "r")
t = open("test.txt", "r")

inputs = []

for line in f:
    inputs.extend([int(x) for x in line.strip().split(" ")])

# Cache results to prevent redundant calcs
cache = {(0,0): 1}

# Calculate length directly instead of numbers
# Branch for each number that split and sum the number of branches
def blink(number, blinks):
    if blinks == 0:
        return 1

    if number == 0:
        return blink(1, blinks-1)

    if (number, blinks) in cache:
        return cache[(number, blinks)]

    if len(str(number))%2 == 0:
        numStr = str(number)
        num1 = int(numStr[:len(numStr)//2])
        num2 = int(numStr[len(numStr)//2:].lstrip("0") or "0")

        result = blink(num1, blinks-1) + blink(num2, blinks-1)
    else:
        result = blink(number*2024, blinks-1)

    cache[(number, blinks)] = result
    return result

output = []

for num in inputs:
    output.append(blink(num, 75))

print(sum(output))