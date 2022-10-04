use primes::{PrimeSet, Sieve};

fn num_divisors(pset: &mut Sieve, mut num: u64) -> u64 {
    // too slow...
    // (1..=num).filter(|i| num % i == 0).count() as u64

    let mut num_divs = 1;

    for prime in pset.iter() {
        if num == 1 {
            break;
        }

        let mut cnt = 0;
        while num % prime == 0 {
            cnt += 1;
            num /= prime;
        }
        num_divs *= cnt + 1;
    }
    return num_divs;
}

fn solve(divisors: u64) -> u64 {
    let mut pset = Sieve::new();
    let mut i = 1;
    let mut total = 0;

    loop {
        total += i;
        i += 1;

        if num_divisors(&mut pset, total) > divisors {
            return total;
        }
    }
}

fn main() {
    // Runs in about 0.210 seconds. Can we do better?
    println!("{}", solve(500));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_num_divisors() {
        let mut pset = Sieve::new();
        assert_eq!(6, num_divisors(&mut pset, 28));
    }

    #[test]
    fn example() {
        assert_eq!(28, solve(5));
    }
}
