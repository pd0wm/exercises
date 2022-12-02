#![feature(test)]

extern crate test;

fn score(round: &(char, char)) -> u64 {
    let (a,b) = round;
    let mut score = match b {
        'X' => 1,
        'Y' => 2,
        'Z' => 3,
        _ => unreachable!(),
    };
    score += match (a, b) {
        ('A', 'X') => 3, // Rock-Rock
        ('A', 'Y') => 6, // Rock-Paper
        ('A', 'Z') => 0, // Rock Scissors
        ('B', 'X') => 0, // Paper-Rock
        ('B', 'Y') => 3, // Paper-Paper
        ('B', 'Z') => 6, // Paper-Scissors
        ('C', 'X') => 6, // Scissors-Rock
        ('C', 'Y') => 0, // Scissors-Paper
        ('C', 'Z') => 3, // Scissors-Scissors
        _ => unreachable!(),
    };
    score
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
        let new_move = match (a, b) {
            ('A', 'X') => (*a, 'Z'), // Rock-Lose -> Scissors
            ('A', 'Y') => (*a, 'X'), // Rock-Draw -> Rock
            ('A', 'Z') => (*a, 'Y'), // Rock Win -> Paper
            ('B', 'X') => (*a, 'X'), // Paper-Lose -> Rock
            ('B', 'Y') => (*a, 'Y'), // Paper-Draw -> Paper
            ('B', 'Z') => (*a, 'Z'), // Paper-Win -> Scissors
            ('C', 'X') => (*a, 'Y'), // Scissors-Lose -> Paper
            ('C', 'Y') => (*a, 'Z'), // Scissors-Draw -> Scissors
            ('C', 'Z') => (*a, 'X'), // Scissors-Win -> Rock
            _ => unreachable!(),
        };
        total_score += score(&new_move);
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
