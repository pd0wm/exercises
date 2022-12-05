#![feature(test)]
#![feature(binary_heap_into_iter_sorted)]

extern crate test;

type Assignment = ((u64, u64), (u64, u64));

fn part1(input: &[Assignment]) -> u64 {
    let mut overlapping = 0;
    for ((a, b), (c, d)) in input {
        if (a <= c && b >= d) || (c <= a && d >= b) {
            overlapping += 1;
        }
    }
    overlapping
}

fn part2(input: &[Assignment]) -> u64 {
    let mut overlapping = 0;
    for ((a, b), (c, d)) in input {
        if (a <= c && b >= c) || (a > c && d >= a) {
            overlapping += 1;
        }
    }
    overlapping
}

fn parse_input() -> Vec<Assignment> {
    let input = include_str!("../../inputs/04.txt").trim();
    let mut output = Vec::new();

    for line in input.lines() {
        if let [left, right] = line.split(',').collect::<Vec<&str>>()[..] {
            if let [a, b] = left.split('-').collect::<Vec<&str>>()[..] {
                if let [c, d] = right.split('-').collect::<Vec<&str>>()[..] {
                    output.push((
                        (a.parse().unwrap(), b.parse().unwrap()),
                        (c.parse().unwrap(), d.parse().unwrap()),
                    ));
                }
            }
        }
    }
    output
}

fn main() {
    let values = parse_input();
    println!("{}", part1(&values));
    println!("{}", part2(&values));
}

#[cfg(test)]
mod day01_tests {
    use super::*;
    use test::{black_box, Bencher};

    #[test]
    fn example() {
        let sample_input = vec![
            ((2, 4), (6, 8)),
            ((2, 3), (4, 5)),
            ((5, 7), (7, 9)),
            ((2, 8), (3, 7)),
            ((6, 6), (4, 6)),
            ((2, 6), (4, 8)),
        ];
        assert_eq!(2, part1(&sample_input));
        assert_eq!(4, part2(&sample_input));
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
