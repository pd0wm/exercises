fn solve(grid_size: u64) -> u64 {
    num::integer::binomial(2 * grid_size, grid_size)
}

fn main() {
    println!("{}", solve(20));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example() {
        assert_eq!(6, solve(2));
    }
}
