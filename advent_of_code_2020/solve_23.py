#!/usr/bin/env python3


def get_cups(cups, curr):
    r = [curr]
    curr = cups[curr]

    while r[0] != curr:
        r.append(curr)
        curr = cups[curr]
    return r


if __name__ == "__main__":
    # part 1
    M, N, O = (100, 916438275, 9)

    # part 2
    M, N, O = (10000000, 916438275, 1000000)

    cups = list(map(int, str(N)))

    for i in range(max(cups) + 1, O+1):
        cups.append(i)

    arr = {}
    for i in range(len(cups)):
        arr[cups[i]] = cups[(i + 1) % len(cups)]


    curr = cups[0]
    for i in range(M):
        label = curr

        a = arr[curr]
        b = arr[a]
        c = arr[b]

        # Remove from list
        arr[curr] = arr[c]

        while True:
            label = label - 1
            if label == 0:
                label = O

            if label not in (a, b, c):
                break

        # Insert in new spot
        n = arr[label]
        arr[label] = a
        arr[c] = n

        # Rotate
        curr = arr[curr]


    # Part 1
    if O == 9:
        print("".join(map(str, get_cups(arr, 1)))[1:])
    # Part 2
    else:
        a = arr[1]
        b = arr[a]
        print(a * b)
