#![feature(test)]
#![feature(binary_heap_into_iter_sorted)]

extern crate test;

use std::collections::BinaryHeap;

fn part1(input: &Vec<Vec<u64>>) -> u64 {
    input.iter().map(|elf| elf.iter().sum()).max().unwrap()
}

fn part2(input: &Vec<Vec<u64>>) -> u64 {
    let sums: BinaryHeap<u64> = input.iter().map(|elf| elf.iter().sum()).collect();
    sums.into_iter_sorted().take(3).sum()
}

fn parse_input() -> Vec<Vec<u64>> {
    let input = include_str!("../../inputs/01.txt").trim();
    input
        .split("\n\n")
        .map(|elf| elf.lines().map(|value| value.parse().unwrap()).collect())
        .collect()
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
            vec![1000, 2000, 3000],
            vec![4000],
            vec![5000, 6000],
            vec![7000, 8000, 9000],
            vec![10000],
        ];
        assert_eq!(24000, part1(&sample_input));
        assert_eq!(45000, part2(&sample_input));
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
