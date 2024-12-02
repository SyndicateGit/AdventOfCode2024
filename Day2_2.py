file = open("Day2.txt", "r")

inputs = []

for line in file:
    array = list(map(int, line.split()))
    inputs.append(array)

total_safe = 0

def rules(levels):
    increasing = None
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if increasing is None:
            increasing = diff > 0
        elif (diff > 0) != increasing:
            return False
    return True

for levels in inputs:
    if rules(levels):
        total_safe += 1
    else:
        for i in range(len(levels)):
            levels_copy = levels.copy()
            levels_copy.pop(i)
            if rules(levels_copy):
                total_safe += 1
                break

print(total_safe)
