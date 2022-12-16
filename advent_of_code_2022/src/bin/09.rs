#![feature(test)]

extern crate test;

use std::collections::HashSet;

enum Direction {
    Up,
    Down,
    Right,
    Left,
}

type Input = Vec<(Direction, usize)>;

fn new_tail(head: &(isize, isize), tail: &(isize, isize)) -> (isize, isize) {
    let dx = head.0 - tail.0;
    let dy = head.1 - tail.1;

    let mut dx_new = dx.signum();
    let mut dy_new = dy.signum();

    if dy.abs() == 2 && dx.abs() != 2 {
        dx_new = 0;
    }

    if dx.abs() == 2 && dy.abs() != 2 {
        dy_new = 0;
    }

    (head.0 - dx_new, head.1 - dy_new)
}

fn solve<const N: usize>(input: &Input) -> u64 {
    let mut head = (0, 0);
    let mut tail = [(0, 0); N];

    let mut tail_visited = HashSet::new();

    for (direction, amount) in input {
        for _ in 0..*amount {
            let (dx, dy) = match direction {
                Direction::Up => (0, 1),
                Direction::Down => (0, -1),
                Direction::Right => (1, 0),
                Direction::Left => (-1, 0),
            };

            head = (head.0 + dx, head.1 + dy);
            tail[N - 1] = new_tail(&head, &tail[N - 1]);

            for i in (0..N - 1).rev() {
                tail[i] = new_tail(&tail[i + 1], &tail[i]);
            }

            tail_visited.insert(tail[0]);
        }
    }

    tail_visited.len() as u64
}

fn part1(input: &Input) -> u64 {
    solve::<1>(input)
}

fn part2(input: &Input) -> u64 {
    solve::<9>(input)
}

fn parse_input() -> Input {
    let input = include_str!("../../inputs/09.txt").trim();
    let mut ret = Vec::new();

    for line in input.lines() {
        if let [direction, amount] = line.split(' ').collect::<Vec<&str>>()[..] {
            let direction = match direction {
                "U" => Direction::Up,
                "D" => Direction::Down,
                "R" => Direction::Right,
                "L" => Direction::Left,
                _ => panic!(),
            };
            let amount = amount.parse().unwrap();
            ret.push((direction, amount));
        }
    }

    ret
}

fn main() {
    let values = parse_input();
    println!("{}", part1(&values));
    println!("{}", part2(&values));
}

#[cfg(test)]
mod day09_tests {
    use super::*;
    use test::{black_box, Bencher};

    #[test]
    fn example() {
        let sample_input: Input = vec![
            (Direction::Right, 4),
            (Direction::Up, 4),
            (Direction::Left, 3),
            (Direction::Down, 1),
            (Direction::Right, 4),
            (Direction::Down, 1),
            (Direction::Left, 5),
            (Direction::Right, 2),
        ];
        assert_eq!(13, part1(&sample_input));
        assert_eq!(1, part2(&sample_input));
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
