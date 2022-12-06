#![feature(test)]

extern crate test;

use itertools::Itertools;

fn find_marker(input: &Vec<char>, length: usize) -> usize {
    for (i, window) in input.windows(length).enumerate() {
        if window.iter().unique().count() == length {
            return i + length;
        }
    }
    panic!("marker not found");
}


fn part1(input: &Vec<char>) -> usize {
    find_marker(input, 4)
}

fn part2(input: &Vec<char>) -> usize {
    find_marker(input, 14)
}

fn parse_input() -> Vec<char> {
    let input = include_str!("../../inputs/06.txt").trim();
    input.chars().collect()
}

fn main() {
    let values = parse_input();
    println!("{}", part1(&values));
    println!("{}", part2(&values));
}

#[cfg(test)]
mod day06_tests {
    use super::*;
    use test::{black_box, Bencher};

    #[test]
    fn example() {
        let sample_input: Vec<char> = "mjqjpqmgbljsphdztnvjfqwrcgsmlb".chars().collect();
        assert_eq!(7, part1(&sample_input));
        assert_eq!(19, part2(&sample_input));
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
