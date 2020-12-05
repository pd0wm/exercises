#!/usr/bin/env python3

def solve_01(numbers):
    for x in numbers:
        for y in numbers:
            if x + y == 2020:
                return x * y

def solve_02(numbers):
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if x + y + z == 2020:
                    return x * y * z

numbers = []
with open('input_01') as f:
    for line in f:
        numbers.append(int(line))

print(solve_01(numbers))
print(solve_02(numbers))

