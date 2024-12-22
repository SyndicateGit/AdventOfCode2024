from collections import deque
from functools import cache

t = open("test.txt", "r")

# Helper functions
def display(list):
    for row in list:
        print("".join(row))

def bound_check(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

inputs = []
for line in t:
    inputs.append(int(line.strip()))

print(inputs)

def mix(secret, number):
    return secret^number

def prune(secret):
    return secret%16777216

def next_secret1(number):
    return prune(mix((number*64), number))

def next_secret2(number):
    return prune(mix((number//32), number))

def next_secret3(number):
    return prune(mix((number*2048), number))


def find_secret(number, n):
    secret = number
    for i in range(n):
        secret = next_secret1(secret)
        secret = next_secret2(secret)
        secret = next_secret3(secret)
    return secret

def calculate():
    total = 0
    for number in inputs:
        total += find_secret(number, 2000)
    return total

print(calculate())