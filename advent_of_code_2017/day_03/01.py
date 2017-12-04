import math
n = 347991

#  Find odd square
s = int(math.sqrt(n))
if s % 2 == 0:
    s -= 1

i = s ** 2 + 1
x = int(s / 2) + 1
y = -int(s / 2)

pos = None
# go up
for _ in range(s):
    y += 1
    i += 1

    if i == n:
        pos = x, y

# go left
for _ in range(s + 1):
    x -= 1
    i += 1

    if i == n:
        pos = x, y

# go down
for _ in range(s + 1):
    y -= 1
    i += 1

    if i == n:
        pos = x, y

# go right
for _ in range(s + 1):
    x += 1
    i += 1

    if i == n:
        pos = x, y
print(pos)
print(abs(pos[0]) + abs(pos[1]))
