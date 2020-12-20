#!/usr/bin/env python3
import numpy as np

MONSTER = "                  # \n#    ##    ##    ###\n #  #  #  #  #  #   "

class Tile:
    def __init__(self, i, rows):
        self.i = i
        self.rows = rows

        self._variants = []

    @property
    def variants(self):
        if self._variants: return self._variants

        for rot in range(4):
            for flip in [False, True]:
                t = np.rot90(self.rows, k=rot)
                if flip:
                    t = np.fliplr(t)
                self._variants.append(Tile(i, t))
        return self._variants

    def fits_right(self, other):
        return (self.rows[0, :] == other.rows[-1, :]).all()

    def fits_below(self, other):
        return (self.rows[:, 0] == other.rows[:, -1]).all()


def fit_tiles(N, tiles, picture):
    if len(picture) == (N * N):
        return picture

    n = len(picture)
    r = []

    if n == 0: # Empty picture
        left = None
        top = None
    elif n < N: # First row, only a tile on the left
        left = picture[n-1]
        top = None
    elif n % N == 0: # Left column, only top tile
        left = None
        top = picture[n - N]
    else:
        left = picture[n - 1]
        top = picture[n - N]

    for i, t in enumerate(tiles):
        leftover = tiles[:i] + tiles[i+1:]
        for t in t.variants:
            if (not left or t.fits_right(left)) and (not top or t.fits_below(top)):
                new_picture = picture + [t]

                r = fit_tiles(N, leftover, new_picture)
                if r is not None:
                    return r
    return None



if __name__ == "__main__":
    np.set_printoptions(linewidth=200)

    # Parse input
    tiles = []
    with open('input_20') as f:
        for line in f:
            line = line.strip()

            # Tile ID
            if line.startswith('Tile'):
                i = int(line.split(' ')[1][:-1])
                rows = []
            else:
                if line:
                    rows.append(list(line))
                else:
                    tiles.append(Tile(i, np.asarray(rows)))
        tiles.append(Tile(i, np.asarray(rows)))

    # Part 1
    N = int(len(tiles)**0.5)
    picture = fit_tiles(N, tiles, [])

    ids = [p.i for p in picture]
    solution_01 = ids[0] * ids[N-1] * ids[N * (N-1)] * ids[N*N-1]
    print(solution_01)

    # Part 2
    full_picture = []
    for r in range(N):
        row = []
        for c in range(N):
            row.append(picture[r * N + c].rows[1:-1, 1:-1])
        full_picture.append(np.vstack(row))
    full_picture = np.hstack(full_picture)

    monster = np.vstack([np.asarray(list(m)) for m in MONSTER.split('\n')])
    monster = monster == '#'

    monsters = 0
    for rot in range(4):
        for flip in [False, True]:
            t = np.rot90(full_picture, k=rot)
            if flip:
                t = np.fliplr(t)

            waves = t == "#"
            for i in range(0, waves.shape[0] - monster.shape[0]):
                for j in range(0, waves.shape[1] - monster.shape[1]):
                    to_check = waves[i:i+monster.shape[0], j:j+monster.shape[1]]
                    to_check = np.logical_and(to_check, monster)
                    if np.all(to_check == monster):
                        monsters += 1


    print(np.sum(waves) - np.sum(monster) * monsters)
