import numpy as np
n = 347991
solution = None


def update_board(board, x, y):
    neighbours = board[y - 1:y + 2, x - 1:x + 2]
    s = neighbours.sum()

    board[y][x] = s

    global solution
    if s > n and solution is None:
        solution = s

    return s


board = np.zeros((10,10))
x = 5
y = 5
l = 2
board[y, x] = 1

x += 1
count = 0
try:
    while True:
        for _ in range(l):
            update_board(board, x, y)
            y -= 1

        y += 1
        x -= 1

        if count != 0:
            l += 1
        for _ in range(l):
            update_board(board, x, y)
            x -= 1

        y += 1
        x += 1
        for _ in range(l):
            update_board(board, x, y)
            y += 1

        x += 1
        y -= 1
        for _ in range(l + 1):
            update_board(board, x, y)
            x += 1

        x -= 1
        y -= 1

        count += 1
        l += 1
except IndexError:
    pass

print x, y
np.set_printoptions(suppress=True, linewidth=200)
print board
print int(solution)
