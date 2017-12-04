from collections import deque
f = open("input_01.txt")

numbers = list(map(int, f.read().rstrip()))
numbers2 = deque(numbers)

numbers2.rotate(int(len(numbers) / 2))

result = 0
for (a, b) in zip(numbers, numbers2):
    if a == b:
        result += a

print(result)
