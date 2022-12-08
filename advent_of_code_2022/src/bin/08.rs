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

fn part2(input: &Input) -> u64 {
    let sz = input.len();
    let mut score = vec![1; sz * sz];

    let mut work: Vec<usize> = Vec::new();
    work.reserve(sz);

    for y in 0..sz {
        for x in 0..sz {
            let cur = if x == sz -1 { 10 } else {input[y][x]};
            while work.len() > 0 && cur >= input[y][work[work.len() - 1]] {
                if let Some(xx) = work.pop() {
                    score[xx + y * sz] *= x - xx;
                }
            }
            work.push(x);
        }

        for x in (0..sz).rev() {
            let cur = if x == 0 { 10 } else {input[y][x]};
            while work.len() > 0 && cur >= input[y][work[work.len() - 1]] {
                if let Some(xx) = work.pop() {
                    score[xx + y * sz] *= xx - x;
                }
            }
            work.push(x);
        }
    }

    for x in 0..sz {
        for y in 0..sz {
            let cur = if y == sz-1 { 10 } else {input[y][x]};
            while work.len() > 0 && cur >= input[work[work.len() - 1]][x] {
                if let Some(yy) = work.pop() {
                    score[x + yy * sz] *= y - yy;
                }
            }
            work.push(y);
        }

        for y in (0..sz).rev() {
            let cur = if y == 0 { 10 } else {input[y][x]};
            while work.len() > 0 && cur >= input[work[work.len() - 1]][x] {
                if let Some(yy) = work.pop() {
                    score[x + yy * sz] *= yy - y;
                }
            }
            work.push(y);
        }
    }

    *score.iter().max().unwrap() as u64
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
