#!/usr/bin/env python3


def english_score(s):
    englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07, ' ': 0.0}

    r = 0.0
    if not all(31 < char < 128 for char in s):
        r -= 1000.0

    for c in s:
        cc = chr(c)
        if cc.upper() in englishLetterFreq:
            r += englishLetterFreq[cc.upper()]
        else:
            r -= 20.0

    return r


if __name__ == "__main__":
    d = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

    solutions = []
    for c in range(32, 128):
        solutions.append(bytes([a ^ c for a in d]))

    for s in sorted(solutions, key=lambda t: english_score(t))[-5:]:
        print(english_score(s), s)
