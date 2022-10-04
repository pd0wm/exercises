use num::bigint::ToBigInt;

fn solve(power: u32) -> u64 {
    let n = 2.to_bigint().unwrap().pow(power);
    n.to_string()
        .chars()
        .map(|x| x.to_digit(10).unwrap() as u64)
        .sum()
}

fn main() {
    println!("{}", solve(1000));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example() {
        assert_eq!(26, solve(15));
    }
}
