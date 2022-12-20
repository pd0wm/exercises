#![feature(test)]

extern crate test;

use itertools::Itertools;

use std::collections::VecDeque;
use std::rc::Rc;

#[derive(Clone)]
struct Monkey {
    cnt: u64,
    items: VecDeque<u64>,
    operation: Rc<dyn Fn(u64) -> u64>,
    test: (u64, usize, usize),
}

type Input = Vec<Monkey>;

fn solve(input: &Input, rounds: usize, divide_by_three: bool) -> u64 {
    let mut input: Input = input.clone();

    let modulo: u64 = input.iter().map(|m| m.test.0).product();

    for _ in 0..rounds {
        for i in 0..input.len() {
            while !input[i].items.is_empty() {
                input[i].cnt += 1;
                let item = input[i].items.pop_front().unwrap();
                let mut item = (input[i].operation)(item);

                if divide_by_three {
                    item = item / 3;
                }

                item = item % modulo;

                let new_i = match item % input[i].test.0 {
                    0 => input[i].test.1,
                    _ => input[i].test.2,
                };
                input[new_i].items.push_back(item);
            }
        }
    }

    input.iter().map(|m| m.cnt).sorted().rev().take(2).product()
}

fn part1(input: &Input) -> u64 {
    solve(input, 20, true)
}

fn part2(input: &Input) -> u64 {
    solve(input, 10_000, false)
}

fn parse_input() -> Input {
    vec![
        Monkey {
            cnt: 0,
            items: VecDeque::from([57, 58]),
            operation: Rc::new(|x| x * 19),
            test: (7, 2, 3),
        },
        Monkey {
            cnt: 0,
            items: VecDeque::from([66, 52, 59, 79, 94, 73]),
            operation: Rc::new(|x| x + 1),
            test: (19, 4, 6),
        },
        Monkey {
            cnt: 0,
            items: VecDeque::from([80]),
            operation: Rc::new(|x| x + 6),
            test: (5, 7, 5),
        },
        Monkey {
            cnt: 0,
            items: VecDeque::from([82, 81, 68, 66, 71, 83, 75, 97]),
            operation: Rc::new(|x| x + 5),
            test: (11, 5, 2),
        },
        Monkey {
            cnt: 0,
            items: VecDeque::from([55, 52, 67, 70, 69, 94, 90]),
            operation: Rc::new(|x| x * x),
            test: (17, 0, 3),
        },
        Monkey {
            cnt: 0,
            items: VecDeque::from([69, 85, 89, 91]),
            operation: Rc::new(|x| x + 7),
            test: (13, 1, 7),
        },
        Monkey {
            cnt: 0,
            items: VecDeque::from([75, 53, 73, 52, 75]),
            operation: Rc::new(|x| x * 7),
            test: (2, 0, 4),
        },
        Monkey {
            cnt: 0,
            items: VecDeque::from([94, 60, 79]),
            operation: Rc::new(|x| x + 2),
            test: (3, 1, 6),
        },
    ]
}

fn main() {
    let values = parse_input();
    println!("{}", part1(&values));
    println!("{}", part2(&values));
}

#[cfg(test)]
mod day11_tests {
    use super::*;
    use test::{black_box, Bencher};

    #[test]
    fn example() {
        let sample_input: Input = vec![
            Monkey {
                cnt: 0,
                items: VecDeque::from([79, 98]),
                operation: Rc::new(|x| x * 19),
                test: (23, 2, 3),
            },
            Monkey {
                cnt: 0,
                items: VecDeque::from([54, 65, 75, 74]),
                operation: Rc::new(|x| x + 6),
                test: (19, 2, 0),
            },
            Monkey {
                cnt: 0,
                items: VecDeque::from([79, 60, 97]),
                operation: Rc::new(|x| x * x),
                test: (13, 1, 3),
            },
            Monkey {
                cnt: 0,
                items: VecDeque::from([74]),
                operation: Rc::new(|x| x + 3),
                test: (17, 0, 1),
            },
        ];
        assert_eq!(10605, part1(&sample_input));
        assert_eq!(2713310158, part2(&sample_input));
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
