f = open("Day1Input.txt", "r")

# Read the two lists
list1 = []
list2 = []

for line in f:
    num1, num2 = line.split()
    list1.append(int(num1))
    list2.append(int(num2))

list2_count = {}

for num in list2:
    if num in list2_count:
        list2_count[num] += 1
    else:
        list2_count[num] = 1

total_distance = 0

for num in list1:
    if num in list2_count:
        total_distance += list2_count[num] * num

print(total_distance)

