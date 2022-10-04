fn collatz_length(mut num: u64) -> u64 {
    let mut len = 1;
    while num != 1 {
        num = match num % 2 == 0 {
            true => num / 2,
            false => 3 * num + 1,
        };
        len += 1;
    }
    len
}

fn solve(max_num: u64) -> u64 {
    (1..max_num)
        .map(|n| (collatz_length(n), n))
        .max()
        .unwrap()
        .1
}

fn main() {
    println!("{}", solve(1_000_000));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_collatz_length() {
        assert_eq!(10, collatz_length(13));
    }
}
