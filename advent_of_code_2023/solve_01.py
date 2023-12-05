#!/usr/bin/env python3

INPUT = 'input_01.txt'
# INPUT = 'input_01_sample_b.txt'

DIGITS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

if __name__ == "__main__":
    with open(INPUT) as f:
        solution_a = 0
        solution_b = 0

        for line in f:
            digits_a = []
            digits_b = []

            for i in range(len(line)):
                if line[i].isdigit():
                    digits_a.append(int(line[i]))
                    digits_b.append(int(line[i]))

                for d, v in DIGITS.items():
                    if line[i:].startswith(d):
                        digits_b.append(v)
                        break

            if digits_a:
                solution_a += 10 * digits_a[0] + digits_a[-1]
            if digits_b:
                solution_b += 10 * digits_b[0] + digits_b[-1]

    print(solution_a)
    print(solution_b)
