use std::fs;
use std::io::{BufRead, BufReader};

fn part1(input: &Vec<Vec<u64>>) -> u64 {
    let sums: Vec<u64> = input.iter().map(|elf| elf.iter().sum()).collect();
    *sums.iter().max().unwrap()
}

fn part2(input: &Vec<Vec<u64>>) -> u64 {
    let mut sums: Vec<u64> = input.iter().map(|elf| elf.iter().sum()).collect();
    sums.sort();
    sums[sums.len() - 3..].iter().sum()
}

fn main() {
    let file = fs::File::open("inputs/01.txt").unwrap();
    let reader = BufReader::new(file);

    let mut values: Vec<Vec<u64>> = vec![];
    values.push(Vec::new());

    for line in reader.lines() {
        let line = line.unwrap();
        if line == "" {
            values.push(Vec::new());
        } else {
            values.last_mut().unwrap().push(line.parse().unwrap());
        }
    }
    println!("{}", part1(&values));
    println!("{}", part2(&values));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example() {
        let sample_input = vec![vec![1000, 2000, 3000], vec![4000], vec![5000, 6000], vec![7000, 8000, 9000], vec![10000]];
        assert_eq!(24000, part1(&sample_input));
        assert_eq!(45000, part2(&sample_input));
    }
}
