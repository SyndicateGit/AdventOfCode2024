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

@cache
def next_secret(number):
    secret = number
    secret = next_secret1(secret)
    secret = next_secret2(secret)
    secret = next_secret3(secret)
    return secret

def find_secret(number, n):
    secrets = []
    secret = number
    for i in range(n):
        secret = next_secret(secret)
        secrets.append(secret%10)
    return secrets

scores = {}
def build_sequence_scores():
    for number in inputs:
        secrets = find_secret(number, 2000)
        prev_secret = secrets[0]
        delta = []
        for secret in secrets:
            delta.append(secret - prev_secret)
            prev_secret = secret
        # print(secrets)
        # print(delta)
        seen = set() # Keep track of seen patterns, only keep first price
        for i in range(len(delta)-3):
            pattern = tuple(delta[i:i+4])
            price = secrets[i+3]
            if pattern not in seen:
                seen.add(pattern)
                if pattern in scores:
                    scores[pattern] += price
                else:
                    scores[pattern] = price
    max_score = 0
    for pattern in scores:
        score = scores[pattern]
        max_score = max(max_score, score)
    print(max_score)
build_sequence_scores()