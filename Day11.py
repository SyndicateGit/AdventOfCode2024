f = open("Day11.txt", "r")
t = open("test.txt", "r")

inputs = []

for line in f:
    inputs.extend([int(x) for x in line.strip().split(" ")])

output = inputs.copy()

def blink(numbers, blinks):
    if blinks == 0:
        print(len(numbers))
        return
    next = []
    for i in range(len(numbers)):
        if numbers[i] == 0:
            next.append(1)
        elif len(str(numbers[i]))%2 == 0:
            numStr = str(numbers[i])
            num1 = numStr[:len(numStr)//2]
            num2 = numStr[len(numStr)//2:]
            # strip num2 of leading zeros
            num2 = num2.lstrip("0")
            if num2 == "":
                num2 = 0
            next.extend([int(num1), int(num2)])
        else:
            next.append(numbers[i]*2024)
    print(blinks)
    blink(next.copy(), blinks-1)

blink(inputs, 75)