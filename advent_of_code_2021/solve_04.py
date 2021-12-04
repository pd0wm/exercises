#!/usr/bin/env python3
import numpy as np

N = 5

class Card:
    def __init__(self, numbers):
        self.numbers = np.asanyarray(numbers).reshape((N, N))
        self.marked = np.zeros_like(self.numbers)

    def won(self):
        columns = np.sum(self.marked, axis=0)
        rows = np.sum(self.marked, axis=1)
        return np.max(columns) == N or np.max(rows) == N

    def unmarked_sum(self):
        return np.sum(self.numbers[self.marked == 0])

    def mark(self, n):
        self.marked[self.numbers == n] = 1
    


if __name__ == "__main__":
    cards = []
    with open('input_04') as f:
        numbers = [int(x) for x in f.readline().strip().split(',')]

        while True:
            if not (x := f.readline()):
                break

            # Parse cards
            s = ""
            for _ in range(N):
                s += f.readline().strip() + " "
            cards.append(Card([int(x) for x in s.strip().split()]))

    first_win = None
    last_win = None
    for n in numbers:
        for c in cards:
            if c.won():
                continue

            c.mark(n)

            if c.won():
                score = n * c.unmarked_sum()
                if first_win is None:
                    first_win = score
                last_win = score

    print(first_win)
    print(last_win)
