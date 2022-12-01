fn part1(input: &Vec<Vec<u64>>) -> u64 {
    input.iter().map(|elf| elf.iter().sum()).max().unwrap()
}

fn part2(input: &Vec<Vec<u64>>) -> u64 {
    let mut sums: Vec<u64> = input.iter().map(|elf| elf.iter().sum()).collect();
    sums.sort();
    sums[sums.len() - 3..].iter().sum()
}

fn main() {
    let input = include_str!("../../inputs/01.txt").trim();
    let values: Vec<Vec<u64>> = input
        .split("\n\n")
        .map(|elf| elf.lines().map(|value| value.parse().unwrap()).collect())
        .collect();

    println!("{}", part1(&values));
    println!("{}", part2(&values));
}

#[cfg(test)]
mod tests {
    use super::*;

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
}
