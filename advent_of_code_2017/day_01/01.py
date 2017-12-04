f = open("input_01.txt")

numbers = list(map(int, f.read().rstrip()))
result = 0
for (a, b) in zip(numbers, numbers[1:] + [numbers[0]]):
    if a == b:
        result += a

print(result)
