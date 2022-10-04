fn solve(sum: u64) -> Option<u64> {
    for a in 0..sum {
        // Ensure a < b < c
        for b in (a + 1)..(sum - a) / 2 {
            let c = sum - a - b;

            if a * a + b * b == c * c {
                return Some(a * b * c);
            }
        }
    }
    return None;
}

fn main() {
    println!("{}", solve(1000).expect("Failed to find solution"));
}
