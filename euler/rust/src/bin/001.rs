fn solve(max: u64) -> u64 {
    let mut sum: u64 = 0;
    for i in 0..max {
        if (i % 3 == 0) || (i % 5 == 0) {
            sum += i;
        }
    }
    return sum;
}

fn main() {
    println!("{}", solve(1000));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example() {
        assert_eq!(23, solve(10));
    }
}
