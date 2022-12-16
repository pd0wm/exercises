#![feature(test)]

extern crate test;

#[derive(Debug)]
enum Instruction {
    Noop,
    Addx(i64),
}

struct Machine {
    cycles: usize,
    x: i64,
    signal_strengths: Vec<i64>,
    crt: Vec<bool>,
}

impl Machine {
    fn new() -> Self {
        Self {
            cycles: 0,
            x: 1,
            signal_strengths: Vec::new(),
            crt: Vec::new(),
        }
    }

    fn run_instruction(&mut self, instruction: &Instruction) {
        match instruction {
            Instruction::Addx(x) => {
                self.cycle();
                self.cycle();
                self.x += x;
            }
            Instruction::Noop => {
                self.cycle();
            }
        };
    }

    fn cycle(&mut self) {
        self.cycles += 1;
        self.signal_strengths.push(self.signal_strength());
        self.crt
            .push((((self.cycles as i64 - 1) % 40) - self.x).abs() <= 1);
    }

    fn run_program(&mut self, instructions: &[Instruction]) {
        instructions.iter().for_each(|i| self.run_instruction(i))
    }

    fn signal_strength(&self) -> i64 {
        (self.cycles as i64) * self.x
    }
}

type Input = Vec<Instruction>;

fn part1(input: &Input) -> i64 {
    let mut machine = Machine::new();
    machine.run_program(input);
    [20, 60, 100, 140, 180, 220]
        .iter()
        .map(|i| machine.signal_strengths[*i - 1])
        .sum()
}

fn part2(input: &Input) -> String {
    let mut ret = String::with_capacity(240);
    let mut machine = Machine::new();
    machine.run_program(input);

    for i in 0..240 {
        if (i > 0) && (i % 40 == 0) {
            ret += "\n";
        }
        if machine.crt[i] {
            ret += "#";
        } else {
            ret += ".";
        }
    }

    ret
}

fn parse_input(input: &str) -> Input {
    let mut ret = Vec::new();
    for line in input.lines() {
        if line.starts_with("noop") {
            ret.push(Instruction::Noop);
        } else if line.starts_with("addx") {
            let val = line.split(' ').last().unwrap();
            ret.push(Instruction::Addx(val.parse().unwrap()));
        }
    }
    ret
}

fn main() {
    let values = parse_input(include_str!("../../inputs/10.txt").trim());
    println!("{}", part1(&values));
    println!("{}", part2(&values));
}

#[cfg(test)]
mod day10_tests {
    use super::*;
    use test::{black_box, Bencher};

    #[test]
    fn example() {
        let sample_input = parse_input(include_str!("../../inputs/10_sample.txt").trim());
        assert_eq!(13140, part1(&sample_input));

        let result = vec![
            "##..##..##..##..##..##..##..##..##..##..",
            "###...###...###...###...###...###...###.",
            "####....####....####....####....####....",
            "#####.....#####.....#####.....#####.....",
            "######......######......######......####",
            "#######.......#######.......#######.....",
        ];
        assert_eq!(result.join("\n"), part2(&sample_input));
    }

    #[bench]
    fn bench_parsing(b: &mut Bencher) {
        b.iter(|| parse_input(include_str!("../../inputs/10.txt").trim()));
    }

    #[bench]
    fn bench_part1(b: &mut Bencher) {
        let values = black_box(parse_input(include_str!("../../inputs/10.txt").trim()));
        b.iter(|| part1(&values));
    }

    #[bench]
    fn bench_part2(b: &mut Bencher) {
        let values = black_box(parse_input(include_str!("../../inputs/10.txt").trim()));
        b.iter(|| part2(&values));
    }
}
