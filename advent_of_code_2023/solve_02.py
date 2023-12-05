#!/usr/bin/env python3
from collections import defaultdict

# INPUT = 'input_02_sample.txt'
INPUT = 'input_02.txt'

def possible(cubes):
    if cubes['red'] > 12:
        return False
    if cubes['green'] > 13:
        return False
    if cubes['blue'] > 14:
        return False
    return True

def max_cubes(cubes_old, cubes_new):
    d = defaultdict(int)
    for k in ['red', 'green', 'blue']:
        d[k] = max(cubes_old[k], cubes_new[k])
    return d


if __name__ == "__main__":
    solution_a = 0
    solution_b = 0

    with open(INPUT) as f:
        for line in f:
            line = line.strip()
            game, cubes = line.split(': ')

            _, game_id = game.split(' ')
            game_id = int(game_id)

            cubes = cubes.split('; ')
            game_possible = True

            min_cubes = defaultdict(int)
            for cc in cubes:

                cube_d = defaultdict(int)
                cc = cc.split(', ')
                for c in cc:
                    amount, color = c.split(' ')
                    amount = int(amount)
                    cube_d[color] = amount

                game_possible = game_possible and possible(cube_d)
                min_cubes = max_cubes(min_cubes, cube_d)

            if game_possible:
                solution_a += game_id

            solution_b += min_cubes['red'] * min_cubes['green'] * min_cubes['blue']

    print(solution_a)
    print(solution_b)

