fn sum_squares(n: u64) -> u64 {
    // (1..=n).map(|x| x*x).sum()
    n * (n + 1) * (2 * n + 1) / 6
}

fn square_sum(n: u64) -> u64 {
    let sum = n * (n + 1) / 2;
    sum * sum
}

fn main() {
    let n = 100;
    println!("{}", square_sum(n) - sum_squares(n));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sum_squares() {
        assert_eq!(385, sum_squares(10));
    }

    #[test]
    fn test_square_sum() {
        assert_eq!(3025, square_sum(10));
    }

    #[test]
    fn example() {
        let n = 10;
        assert_eq!(2640, square_sum(n) - sum_squares(n));
    }
}
