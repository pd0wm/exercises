#![feature(test)]

use std::collections::HashMap;

extern crate test;

type Input = Vec<i64>;

fn part1(input: &Input) -> u64 {
    // let new_idx: Vec<i64>= input.iter().enumerate().map(|(i, x)| ((i as i64) + x)).collect();

    // println!("{:?}", new_idx);
    let n = input.len();

    // Map from idx to next idx
    let mut map: HashMap<usize, usize> = HashMap::new();
    for (i, _) in input.iter().enumerate() {
        map.insert(i, (i + 1) % n);
    }

    for (i, x) in input.iter().enumerate() {
        cur_idx = map.get(i);
    }
    0

}

fn part2(_input: &Input) -> u64 {
    0
}

fn parse_input() -> Input {
    Input::default()
}

fn main() {
    let values = parse_input();
    println!("{}", part1(&values));
    println!("{}", part2(&values));
}

#[cfg(test)]
mod day20_tests {
    use super::*;
    use test::{black_box, Bencher};

    #[test]
    fn example() {
        let sample_input = vec![1, 2, -3, 3, -2, 0, 4];
        assert_eq!(3, part1(&sample_input));
        assert_eq!(0, part2(&sample_input));
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
