#![feature(test)]

use std::collections::VecDeque;

extern crate test;

fn part1(init: &Vec<VecDeque<char>>, moves: &Vec<(usize, usize, usize)>) -> String {
    let mut state = init.clone();

    for (n, from, to) in moves {
        for _ in 0..*n {
            let c: char = state[*from - 1].pop_back().unwrap();
            state[*to - 1].push_back(c);
        }
    }
    state.iter().map(|s| s.back().unwrap()).collect()
}

fn part2(init: &Vec<VecDeque<char>>, moves: &Vec<(usize, usize, usize)>) -> String {
    let mut state = init.clone();
    let mut tmp_stack = VecDeque::new(); // Using a tmp stack is faster than VecDeque::split_off()

    for (n, from, to) in moves {
        for _ in 0..*n {
            let c: char = state[*from - 1].pop_back().unwrap();
            tmp_stack.push_back(c);
        }
        for _ in 0..*n {
            let c: char = tmp_stack.pop_back().unwrap();
            state[*to - 1].push_back(c);
        }
    }
    state.iter().map(|s| s.back().unwrap()).collect()
}

fn parse_input() -> (Vec<VecDeque<char>>, Vec<(usize, usize, usize)>) {
    let init: Vec<VecDeque<char>> = vec![
        VecDeque::from(['S', 'T', 'H', 'F', 'W', 'R']),
        VecDeque::from(['S', 'G', 'D', 'Q', 'W']),
        VecDeque::from(['B', 'T', 'W']),
        VecDeque::from(['D', 'R', 'W', 'T', 'N', 'Q', 'Z', 'J']),
        VecDeque::from(['F', 'B', 'H', 'G', 'L', 'V', 'T', 'Z']),
        VecDeque::from(['L', 'P', 'T', 'C', 'V', 'B', 'S', 'G']),
        VecDeque::from(['Z', 'B', 'R', 'T', 'W', 'G', 'P']),
        VecDeque::from(['N', 'G', 'M', 'T', 'C', 'J', 'R']),
        VecDeque::from(['L', 'G', 'B', 'W']),
    ];

    let input = include_str!("../../inputs/05.txt").trim();
    let moves = input
        .lines()
        .skip(10)
        .map(|line| {
            if let &[_, n, _, from, _, to] = &line.split(' ').collect::<Vec<&str>>()[..] {
                (
                    n.parse().unwrap(),
                    from.parse().unwrap(),
                    to.parse().unwrap(),
                )
            } else {
                panic!("malformed input");
            }
        })
        .collect();
    (init, moves)
}

fn main() {
    let (init, moves) = parse_input();
    println!("{}", part1(&init, &moves));
    println!("{}", part2(&init, &moves));
}

#[cfg(test)]
mod day05_tests {
    use super::*;
    use test::{black_box, Bencher};

    #[test]
    fn example() {
        let init: Vec<VecDeque<char>> = vec![
            VecDeque::from(['Z', 'N']),
            VecDeque::from(['M', 'C', 'D']),
            VecDeque::from(['P']),
        ];
        let moves = vec![(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)];
        assert_eq!("CMZ", part1(&init, &moves));
        assert_eq!("MCD", part2(&init, &moves));
    }

    #[bench]
    fn bench_parsing(b: &mut Bencher) {
        b.iter(|| parse_input());
    }

    #[bench]
    fn bench_part1(b: &mut Bencher) {
        let (init, moves) = black_box(parse_input());
        b.iter(|| part1(&init, &moves));
    }

    #[bench]
    fn bench_part2(b: &mut Bencher) {
        let (init, moves) = black_box(parse_input());
        b.iter(|| part2(&init, &moves));
    }
}
