
fn solve(max: u64) -> u64 {
    let mut r = 1;
    for i in 1..=max {
        r = num::integer::lcm(r, i);
    }
    return r;
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
