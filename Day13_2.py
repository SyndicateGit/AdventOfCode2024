from Day8 import letter

f = open("Day13.txt", "r")
t = open("test.txt", "r")

inputs = []

for line in f:
    l = line.strip().split(" ")
    if l == [""]:
        continue
    inputs.append(l)

print(inputs)
# Button press price
At = 3
Bt = 1


def linear(Ax, Ay, Bx, By, Px, Py):
    A = (Px * By - Py * Bx) / (Ax * By - Ay * Bx)
    B = (Px * Ay - Py * Ax) / (Bx * Ay - By * Ax)

    return A, B

def min_tokens(Ax, Ay, Bx, By, Px, Py):
    # Ax(A) + Bx(B) = Px
    # Ay(A) + By(B) = Py
    # A = (Px*By - Py*Bx)/(Ax*By - Ay*Bx)
    # B = (Px*Ay - Py*Ax)/(Bx*Ay - By*Ax)

    A, B = linear(Ax, Ay, Bx, By, Px, Py)

    # Invalid combination when decimal
    if A % 1 != 0 or B % 1 != 0:
        return 0

    return 3*A + B



def test():
    total = 0
    for i in range(0, len(inputs), 3):
        print(inputs[i])
        Ax = int(inputs[i][2].split("+")[1].replace(',', ''))
        Ay = int(inputs[i][3].split("+")[1].replace(',', ''))
        Bx = int(inputs[i+1][2].split("+")[1].replace(',', ''))
        By = int(inputs[i+1][3].split("+")[1].replace(',', ''))
        Px = int(inputs[i+2][1].split("=")[1].replace(',', ''))
        Py = int(inputs[i+2][2].split("=")[1].replace(',', ''))
        total += min_tokens(Ax, Ay, Bx, By, Px + 10000000000000, Py + 10000000000000)
    print(total)
test()