import functools

file = open("Day5.txt", "r")
test_file = open("test.txt", "r")

orders = []
updates = []
for line in file:
    if line.count("|") == 1:
        orders.append([int(line.split("|")[0].strip()), int(line.split("|")[1].strip())])
    elif line.count(",") == 0:
        continue
    else:
        updates.append([int(x) for x in line.strip().split(",") if x.isnumeric()])

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

incorrect_updates = []

def check_order(index, update):
    num = update[index]
    for i in range(0, index):
        if num not in dict_before:
            return False
        if update[i] not in dict_before[num]:
            return False
    for i in range(index + 1, len(update)):
        if num not in dict_after:
            return False
        if update[i] not in dict_after[num]:
            return False
    return True

def check_update(update):
    for i in range(len(update)):
        if not check_order(i, update):
            return False
    return True

for update in updates:
    if not check_update(update):
        incorrect_updates.append(update)


def order_incorrect_update(incorrect_update):
    return sorted(incorrect_update, key=functools.cmp_to_key(compare_order))

def compare_order(num1, num2):
    if num1 in dict_before and num2 in dict_before[num1]:
        return -1
    elif num2 in dict_before and num1 in dict_before[num2]:
        return 1
    else:
        return 0

print(incorrect_updates)

sum = 0
for update in incorrect_updates:
    ordered = order_incorrect_update(update)
    mid = len(ordered) // 2
    sum += ordered[mid]

print(sum)
