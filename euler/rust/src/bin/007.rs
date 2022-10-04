fn is_prime(n: u64) -> bool{
    let mut i = 2u64;

    if n == 1 {
        return false;
    }

    while i * i <= n {
        if n % i == 0 {
            return  false;
        }
        i += 1;
    }
    return true;
}

fn nth_prime(n: u64) -> u64 {
    let mut cnt = 0u64;
    let mut i = 0u64;

    while cnt < n {
        i += 1;
        if is_prime(i) {
            cnt += 1;
        }
    }

    return i;
}


fn main() {
    println!("{}", nth_prime(10_001));
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example() {
        assert_eq!(13, nth_prime(6));
    }
}
