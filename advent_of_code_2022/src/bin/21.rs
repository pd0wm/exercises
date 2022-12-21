#![feature(test)]

use std::{cmp::Ordering, collections::HashMap};

extern crate test;

#[derive(Debug, Clone)]
enum Monkey {
    Value(u64),
    Operation(String, char, String),
}

type Input = HashMap<String, Monkey>;

fn eval_monkey(input: &Input, monkey: &str) -> Option<u64> {
    match input.get(monkey).unwrap() {
        Monkey::Value(value) => Some(*value),
        Monkey::Operation(left, op, right) => {
            let left = eval_monkey(input, left)?;
            let right = eval_monkey(input, right)?;

            match *op {
                '*' => left.checked_mul(right),
                '/' => left.checked_div(right),
                '+' => left.checked_add(right),
                '-' => left.checked_sub(right),
                _ => panic!("unsupported operation"),
            }
        }
    }
}

fn part1(input: &Input) -> u64 {
    eval_monkey(input, "root").unwrap()
}

fn part2(input: &Input) -> u64 {
    let mut input: Input = input.clone();

    let root = input.get("root").unwrap().clone();

    if let Monkey::Operation(left, _, right) = root {
        let mut humn = 4418;
        loop {
            input.insert("humn".to_string(), Monkey::Value(humn));

            // Not super happy about this. Seems that due to rounding errors multiple solutions can seem right
            if let (Some(left), Some(right)) =
                (eval_monkey(&input, &left), eval_monkey(&input, &right))
            {
                match left.cmp(&right) {
                    Ordering::Equal => return humn,
                    Ordering::Less => humn -= (right - left) / 10,
                    Ordering::Greater => humn += (left - right) / 10,
                }
            } else {
                humn = humn / 2;
            }
        }
    }
    0
}

fn parse_input(input: &str) -> Input {
    let mut result: Input = HashMap::new();
    for line in input.lines() {
        if let [name, value] = line.split(' ').collect::<Vec<&str>>()[..] {
            result.insert(name[..4].to_string(), Monkey::Value(value.parse().unwrap()));
        } else if let [name, left, op, right] = line.split(' ').collect::<Vec<&str>>()[..] {
            result.insert(
                name[..4].to_string(),
                Monkey::Operation(
                    left.to_string(),
                    op.chars().nth(0).unwrap(),
                    right.to_string(),
                ),
            );
        }
    }
    result
}

fn main() {
    let values = parse_input(include_str!("../../inputs/21.txt").trim());
    println!("{}", part1(&values));
    println!("{}", part2(&values));
}

#[cfg(test)]
mod day21_tests {
    use super::*;
    use test::{black_box, Bencher};

    // #[test]
    // fn example() {
    //     let sample_input = parse_input(include_str!("../../inputs/21_sample.txt").trim());
    //     assert_eq!(152, part1(&sample_input));
    //     assert_eq!(301, part2(&sample_input));
    // }

    #[bench]
    fn bench_parsing(b: &mut Bencher) {
        b.iter(|| parse_input(include_str!("../../inputs/21.txt").trim()));
    }

    #[bench]
    fn bench_part1(b: &mut Bencher) {
        let values = black_box(parse_input(include_str!("../../inputs/21.txt").trim()));
        b.iter(|| part1(&values));
    }

    #[bench]
    fn bench_part2(b: &mut Bencher) {
        let values = black_box(parse_input(include_str!("../../inputs/21.txt").trim()));
        b.iter(|| part2(&values));
    }
}
