file = open("Day5.txt", "r")

orders = []
updates = []
for line in file:
    if line.count("|") == 1:
        orders.append([int(line.split("|")[0].strip()), int(line.split("|")[1].strip())])
    elif line.count(",") == 0:
        continue
    else:
        updates.append([int(x) for x in line.split(",") if x.isnumeric()])

print(orders)
print(updates)

dict_before = {}
dict_after = {}

for order in orders:
    if order[1] not in dict_before:
        dict_before[order[1]] = [order[0]]
    else:
        dict_before[order[1]].append(order[0])
    if order[0] not in dict_after:
        dict_after[order[0]] = [order[1]]
    else:
        dict_after[order[0]].append(order[1])


correct_updates = []


def check_order(index, update):
    num = update[index]

    if num not in dict_before and num not in dict_after:
        return False

    for i in range(0, index): # Check before
        if num not in dict_before or update[i] not in dict_before[num]:
            return False

    for i in range(index + 1, len(update)): # Check after
        if num not in dict_after or update[i] not in dict_after[num]:
            return False

    return True

for update in updates:
    correct = True
    for i in range(len(update)):
        if not check_order(i, update):
            correct = False
            break
    if not correct:
        correct_updates.append(update)

sum = 0
for update in correct_updates:
    mid = len(update) // 2
    sum += update[mid]

print(sum)