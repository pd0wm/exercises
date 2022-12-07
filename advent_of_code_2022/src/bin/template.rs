#![feature(test)]

extern crate test;

type Input = ();

fn part1(_input: &Input) -> u64 {
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
mod dayxx_tests {
    use super::*;
    use test::{black_box, Bencher};

    #[test]
    fn example() {
        let sample_input: Input = Input::default();
        assert_eq!(0, part1(&sample_input));
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
