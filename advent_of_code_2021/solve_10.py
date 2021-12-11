#!/usr/bin/env python3

OPEN = '([{<'
CLOSE = ')]}>'
POINTS_01 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
POINTS_02 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

part_01 = 0
part_02 = []
for chunk in open('input_10'):
    open_stack = []
    corrupt = False
    for c in chunk.strip():
        if c in OPEN:
            last_open = c
            open_stack.append(c)
        elif OPEN[CLOSE.index(c)] != open_stack.pop():
            # Corrupted
            part_01 += POINTS_01[c]
            corrupt = True
            break

    if not corrupt:
        close_stack = [CLOSE[OPEN.index(c)] for c in reversed(open_stack)]
        score = 0
        for c in close_stack:
            score = (score * 5) + POINTS_02[c]
        part_02.append(score)
        
print(part_01)
print(sorted(part_02)[len(part_02) // 2])