fn solve(max: u64) -> u64 {
    (1..=max).fold(1, |r, i| num::integer::lcm(r, i))
}

fn main() {
    println!("{}", solve(20))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example() {
        assert_eq!(2520, solve(10));
    }
}
