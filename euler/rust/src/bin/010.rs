use primes::PrimeSet;

fn solve(max: u64) -> u64 {
    let mut p = primes::Sieve::new();
    p.iter().take_while(|x| x < &max).sum()
}

fn main() {
    println!("{}", solve(2_000_000));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example() {
        assert_eq!(17, solve(10));
    }
}
