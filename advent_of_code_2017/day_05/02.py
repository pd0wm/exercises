f = open("input_01.txt")

instructions = map(int, f.read().rstrip().split('\n'))
p = 0
i = 0

while True:
    try:
        jump = instructions[p]
    except IndexError:
        break

    if jump >= 3:
        instructions[p] -= 1
    else:
        instructions[p] += 1

    p += jump
    i += 1

print i
