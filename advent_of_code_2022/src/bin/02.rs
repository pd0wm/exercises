#![feature(test)]

extern crate test;

fn score(round: &(char, char)) -> u64 {
    match round {
        ('A', 'X') => 3 + 1, // Rock-Rock
        ('A', 'Y') => 6 + 2, // Rock-Paper
        ('A', 'Z') => 0 + 3, // Rock Scissors
        ('B', 'X') => 0 + 1, // Paper-Rock
        ('B', 'Y') => 3 + 2, // Paper-Paper
        ('B', 'Z') => 6 + 3, // Paper-Scissors
        ('C', 'X') => 6 + 1, // Scissors-Rock
        ('C', 'Y') => 0 + 2, // Scissors-Paper
        ('C', 'Z') => 3 + 3, // Scissors-Scissors
        _ => unreachable!(),
    }
}

fn part1(input: &[(char, char)]) -> u64 {
    let mut total_score = 0;
    for round in input {
        total_score += score(round);
    }
    total_score
}

fn part2(input: &[(char, char)]) -> u64 {
    let mut total_score = 0;
    for (a, b) in input {
        total_score += match (a, b) {
            ('A', 'X') => score(&('A', 'Z')), // Rock-Lose -> Scissors
            ('A', 'Y') => score(&('A', 'X')), // Rock-Draw -> Rock
            ('A', 'Z') => score(&('A', 'Y')), // Rock Win -> Paper
            ('B', 'X') => score(&('B', 'X')), // Paper-Lose -> Rock
            ('B', 'Y') => score(&('B', 'Y')), // Paper-Draw -> Paper
            ('B', 'Z') => score(&('B', 'Z')), // Paper-Win -> Scissors
            ('C', 'X') => score(&('C', 'Y')), // Scissors-Lose -> Paper
            ('C', 'Y') => score(&('C', 'Z')), // Scissors-Draw -> Scissors
            ('C', 'Z') => score(&('C', 'X')), // Scissors-Win -> Rock
            _ => unreachable!(),
        };
    }
    total_score
}

fn parse_input() -> Vec<(char, char)> {
    let input = include_str!("../../inputs/02.txt").trim();
    input
        .lines()
        .map(|line| (line.chars().nth(0).unwrap(), line.chars().nth(2).unwrap()))
        .collect()
}

fn main() {
    let values = parse_input();
    println!("{}", part1(&values));
    println!("{}", part2(&values));
}

#[cfg(test)]
mod day02_tests {
    use super::*;
    use test::{black_box, Bencher};

    #[test]
    fn example() {
        let sample_input = vec![('A', 'Y'), ('B', 'X'), ('C', 'Z')];
        assert_eq!(15, part1(&sample_input));
        assert_eq!(12, part2(&sample_input));
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
