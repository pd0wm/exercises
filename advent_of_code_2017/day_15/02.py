A = 591
B = 393

a_val = []
b_val = []

while True:
    A *= 16807
    B *= 48271

    A = A % 2147483647
    B = B % 2147483647

    if A % 4 == 0:
        a_val.append(A)

    if B % 8 == 0:
        b_val.append(B)

    if min(len(a_val), len(b_val)) == 5000000:
        break

total = 0
for a, b in zip(a_val, b_val):
    if a & 0xFFFF == b & 0xFFFF:
        total += 1

print total
