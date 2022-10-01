fn largest_factor(mut num: u64) -> u64 {
    let mut i = 2;
    while i * i <= num {
        if num % i != 0 {
            i += 1;
        } else {
            num = num / i;
        }
    }
    return num;
}

fn main() {
    println!("{}", largest_factor(6_00_851_475_143))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example() {
        assert_eq!(29, largest_factor(13195));
    }
}
