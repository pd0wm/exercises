fn solve(max: u64) -> u64 {
    let mut a = 1u64;
    let mut b = 2u64;
    let mut sum = b;

    while b < max {
        (a, b) = (b, a + b);

        // Sum even fibonacci terms
        if b % 2 == 0 {
            sum += b;
        }
    }
    return sum;
}

fn main() {
    println!("{}", solve(4_000_000));
}
