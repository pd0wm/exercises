import numpy as np

banks = map(int, open('input_01.txt').read().rstrip().split('\t'))
# banks = [0, 2, 7, 0]
history = []
l = len(banks)

its = 0

while True:
    i = np.argmax(banks)

    n = banks[i]
    banks[i] = 0
    i += 1

    while n:
        banks[i % l] += 1
        i += 1
        n -= 1

    its += 1

    if banks in history:
        print "Part 2:"
        print len(history) - history.index(banks)
        break

    history.append(banks[:])

print "Part 1:"
print its
