#!/usr/bin/env python3


instructions = [(instruction[0], int(instruction[1])) for ln in open('input_02') if (instruction := ln.strip().split(' '))]

# Part one
depth = 0
horizontal = 0
for move, n in instructions:
    if move == 'forward':
        horizontal += n
    elif move == 'up':
        depth -= n
    elif move == 'down':
        depth += n
print(depth * horizontal)


# Part two
aim = 0
depth = 0
horizontal = 0
for move, n in instructions:
    if move == 'forward':
        horizontal += n
        depth += aim * n
    elif move == 'up':
        aim -= n
    elif move == 'down':
        aim += n
print(depth * horizontal)
