A = 591
B = 393

total = 0
for i in range(40000000):
    A *= 16807
    B *= 48271

    A = A % 2147483647
    B = B % 2147483647

    if A & 0xFFFF == B & 0xFFFF:
        total += 1

print total
