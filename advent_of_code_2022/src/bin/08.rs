#![feature(test)]
use std::cmp::max;

extern crate test;

type Input = Vec<Vec<i32>>;

fn part1(input: &Input) -> u64 {
    let sz = input.len();
    let mut visible = vec![0; sz * sz];

    // left - right
    for y in 0..sz {
        let mut highest = -1;
        for x in 0..sz {
            if input[y][x] > highest {
                visible[x + y * sz] = 1;
            }
            highest = max(highest, input[y][x]);
        }

        highest = -1;
        for x in (0..sz).rev() {
            if input[y][x] > highest {
                visible[x + y * sz] = 1;
            }
            highest = max(highest, input[y][x]);
        }
    }

    // top - bottom
    for x in 0..sz {
        let mut highest = -1;
        for y in 0..sz {
            if input[y][x] > highest {
                visible[x + y * sz] = 1;
            }
            highest = max(highest, input[y][x]);
        }
        highest = -1;
        for y in (0..sz).rev() {
            if input[y][x] > highest {
                visible[x + y * sz] = 1;
            }
            highest = max(highest, input[y][x]);
        }
    }

    visible.iter().sum()
}

fn scenic_score(input: &Input, x: i64, y: i64) -> u64 {
    let sz = input.len() as i64;

    let mut score = 1;

    let height = input[y as usize][x as usize];

    for (i, x) in (x + 1..sz + 1).enumerate() {
        if x == sz {
            score *= i;
            break;
        } else if input[y as usize][x as usize] >= height {
            score *= i + 1;
            break;
        }
    }
    for (i, x) in (-1..x).rev().enumerate() {
        if x == -1 {
            score *= i;
            break;
        } else if input[y as usize][x as usize] >= height {
            score *= i + 1;
            break;
        }
    }
    for (i, y) in (y + 1..sz + 1).enumerate() {
        if y == sz {
            score *= i;
            break;
        } else if input[y as usize][x as usize] >= height {
            score *= i + 1;
            break;
        }
    }
    for (i, y) in (-1..y).rev().enumerate() {
        if y == -1 {
            score *= i;
            break;
        } else if input[y as usize][x as usize] >= height {
            score *= i + 1;
            break;
        }
    }

    score as u64
}

fn part2(input: &Input) -> u64 {
    let sz = input.len() as i64;
    (1..sz - 1)
        .map(|y| {
            (1..sz - 1)
                .map(|x| scenic_score(input, x, y))
                .max()
                .unwrap()
        })
        .max()
        .unwrap()
}

fn parse_input() -> Input {
    let input = include_str!("../../inputs/08.txt").trim();
    input
        .lines()
        .map(|l| l.chars().map(|c| c.to_digit(10).unwrap() as i32).collect())
        .collect()
}

fn main() {
    let values = parse_input();
    println!("{}", part1(&values));
    println!("{}", part2(&values));
}

#[cfg(test)]
mod day08_tests {
    use super::*;
    use test::{black_box, Bencher};

    #[test]
    fn example() {
        let sample_input = vec![
            vec![3, 0, 3, 7, 3],
            vec![2, 5, 5, 1, 2],
            vec![6, 5, 3, 3, 2],
            vec![3, 3, 5, 4, 9],
            vec![3, 5, 3, 9, 0],
        ];
        assert_eq!(21, part1(&sample_input));
        assert_eq!(4, scenic_score(&sample_input, 2, 1));
        assert_eq!(8, part2(&sample_input));
    }

    #[bench]
    fn bench_parsing(b: &mut Bencher) {
        b.iter(|| parse_input());
    }

    #[bench]
    fn bench_part1(b: &mut Bencher) {
        let values = black_box(parse_input());
        b.iter(|| part1(&values));
    }

    #[bench]
    fn bench_part2(b: &mut Bencher) {
        let values = black_box(parse_input());
        b.iter(|| part2(&values));
    }
}
