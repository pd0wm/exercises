#![feature(test)]
use std::cmp::Ordering;

use bisection::bisect_left;

extern crate test;

#[derive(Debug, Eq, PartialEq, Clone)]
enum Packet {
    Int(u64),
    List(Vec<Packet>),
}

impl From<&str> for Packet {
    fn from(packet: &str) -> Self {
        if packet.starts_with('[') {
            let mut packets = Vec::new();

            if packet.len() > 2 {
                let mut depth = 0;
                let mut prev_i = 0;

                // Find items boundaries, making sure to ignore nested commas
                for (i, c) in packet.chars().enumerate() {
                    match c {
                        '[' => depth += 1,
                        ']' => depth -= 1,
                        ',' => {
                            if depth == 1 {
                                packets.push(packet[prev_i + 1..i].into());
                                prev_i = i;
                            }
                        }
                        _ => {}
                    }
                }
                packets.push(packet[prev_i + 1..packet.len() - 1].into());
            }

            Packet::List(packets)
        } else {
            Packet::Int(packet.parse().unwrap())
        }
    }
}

impl PartialOrd for Packet {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Packet {
    fn cmp(&self, other: &Self) -> Ordering {
        match (self, other) {
            (Packet::Int(a), Packet::Int(b)) => a.cmp(b),
            (Packet::List(a), Packet::List(b)) => {
                for i in 0..a.len() {
                    if i >= b.len() {
                        return Ordering::Greater;
                    }

                    if a[i] < b[i] {
                        return Ordering::Less;
                    }

                    if a[i] > b[i] {
                        return Ordering::Greater;
                    }
                }

                if a.len() < b.len() {
                    return Ordering::Less;
                }

                Ordering::Equal
            }
            (Packet::List(_), b) => {
                let b = Packet::List(vec![b.clone()]);
                self.cmp(&b)
            }
            (a, Packet::List(_)) => {
                let a = Packet::List(vec![a.clone()]);
                a.cmp(other)
            }
        }
    }
}

type Input = Vec<(Packet, Packet)>;

fn part1(input: &Input) -> u64 {
    input
        .iter()
        .enumerate()
        .map(|(i, (a, b))| if a < b { i as u64 + 1 } else { 0 })
        .sum()
}

fn part2(input: &Input) -> u64 {
    let mut all = Vec::new();
    for (a, b) in input.iter() {
        all.push(a);
        all.push(b);
    }

    all.sort();

    let a = bisect_left(&all, &&"[[2]]".into()) as u64;
    let b = bisect_left(&all, &&"[[6]]".into()) as u64;

    (a + 1) * (b + 2)
}

fn parse_input(input: &str) -> Input {
    let mut lines = input.lines();
    let mut ret = Vec::new();

    while let (Some(a), Some(b), _) = (lines.next(), lines.next(), lines.next()) {
        ret.push((a.into(), b.into()));
    }
    ret
}

fn main() {
    let values = parse_input(include_str!("../../inputs/13.txt").trim());
    println!("{}", part1(&values));
    println!("{}", part2(&values));
}

#[cfg(test)]
mod day13_tests {
    use super::*;
    use test::{black_box, Bencher};

    #[test]
    fn example() {
        let sample_input = parse_input(include_str!("../../inputs/13_sample.txt").trim());
        assert_eq!(13, part1(&sample_input));
        assert_eq!(140, part2(&sample_input));
    }

    #[bench]
    fn bench_parsing(b: &mut Bencher) {
        b.iter(|| parse_input(include_str!("../../inputs/13.txt").trim()));
    }

    #[bench]
    fn bench_part1(b: &mut Bencher) {
        let values = black_box(parse_input(include_str!("../../inputs/13.txt").trim()));
        b.iter(|| part1(&values));
    }

    #[bench]
    fn bench_part2(b: &mut Bencher) {
        let values = black_box(parse_input(include_str!("../../inputs/13.txt").trim()));
        b.iter(|| part2(&values));
    }
}
