fn is_palindrome(num: u64) -> bool {
    let s = num.to_string();
    s.chars().eq(s.chars().rev())
}

fn solve(max_digits: u32) -> u64 {
    let max = 10u64.pow(max_digits);
    let mut largest = 0u64;
    for a in 0..max {
        for b in 0..max {
            if is_palindrome(a * b) {
                largest = std::cmp::max(largest, a * b);
            }
        }
    }
    return largest;
}


fn main() {
    println!("{}", solve(3))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example() {
        assert_eq!(9009, solve(2));
    }

    #[test]
    fn palindrome() {
        assert_eq!(true, is_palindrome(99099));
        assert_eq!(false, is_palindrome(12345));
    }
}
