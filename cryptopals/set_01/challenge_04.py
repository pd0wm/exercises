#!/usr/bin/env python3
import scipy.stats
from collections import Counter


def is_printable(s):
    if s in [ord('\n'), ord('\t'), ord('\r')]:
        return True
    if s < 32:
        return False

    return True


def english_score(s):
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    english_letter_freq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

    num_printable = 0
    num_good_chars = 0
    for c in s:
        if is_printable(c):
            num_printable += 1
        if chr(c).upper() in ALPHABET:
            num_good_chars += 1

    if num_printable < 0.95 * len(s):
        return -1

    counts = Counter([chr(c).upper() for c in s])
    actual = [counts.get(c, 0) for c in ALPHABET]
    expected = [english_letter_freq[c] / 100. * num_good_chars for c in ALPHABET]

    _, p = scipy.stats.chisquare(actual, expected)
    return p + num_good_chars / len(s)


if __name__ == "__main__":
    d = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

    solutions = []
    for c in range(32, 128):
        solutions.append(bytes([a ^ c for a in d]))

    for s in sorted(solutions, key=lambda t: english_score(t))[-5:]:
        print(english_score(s), s)
