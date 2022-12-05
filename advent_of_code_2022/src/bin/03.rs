#![feature(test)]

extern crate test;

fn priority(item: &char) -> u8 {
    if item.is_lowercase() {
        (*item as u8) - ('a' as u8)
    } else {
        (*item as u8) - ('A' as u8) + 26
    }
}

fn get_hash(input: &[char]) -> u64 {
    input
        .iter()
        .fold(0u64, |acc, c| acc | (1u64 << priority(c)))
}

fn part1(input: &[Vec<char>]) -> u64 {
    let mut total = 0u64;
    for line in input {
        let first = get_hash(&line[..line.len() / 2]);
        let second = get_hash(&line[line.len() / 2..]);
        let shared = first & second;

        total += (u64::BITS - shared.leading_zeros()) as u64;
    }
    total
}

fn part2(input: &[Vec<char>]) -> u64 {
    let mut total = 0u64;
    for chunk in input.chunks(3) {
        if let [a, b, c] = chunk {
            let (a, b, c) = (get_hash(&a), get_hash(&b), get_hash(&c));
            let shared = a & b & c;
            total += (u64::BITS - shared.leading_zeros()) as u64;
        }
    }
    total
}

fn parse_input() -> Vec<Vec<char>> {
    let input = include_str!("../../inputs/03.txt").trim();
    input.lines().map(|s| s.chars().collect()).collect()
}

fn main() {
    let values = parse_input();
    println!("{}", part1(&values));
    println!("{}", part2(&values));
}

#[cfg(test)]
mod day03_tests {
    use super::*;
    use test::{black_box, Bencher};

    #[test]
    fn example() {
        let sample_input = [
            "vJrwpWtwJgWrhcsFMMfFFhFp".chars().collect(),
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL".chars().collect(),
            "PmmdzqPrVvPwwTWBwg".chars().collect(),
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn".chars().collect(),
            "ttgJtRGJQctTZtZT".chars().collect(),
            "CrZsJsPPZsGzwwsLwLmpwMDw".chars().collect(),
        ];
        assert_eq!(157, part1(&sample_input));
        assert_eq!(70, part2(&sample_input));
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
