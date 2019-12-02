use std::env;
use std::cmp::max;

use advent::read_input;


fn compute_fuel(mass : &i64) -> i64 {
    return max(mass / 3 - 2, 0);
}

fn compute_total_fuel(mass : &i64) -> i64 {
    let mut total = 0;
    let mut fuel = compute_fuel(mass);

    while fuel != 0 {
        total += fuel;
        fuel = compute_fuel(&fuel);
    }

    return total;
}

fn part_one(input : &Vec<i64>) -> i64{
    return input.into_iter().map(compute_fuel).sum();
}

fn part_two(input : &Vec<i64>) -> i64{
    return input.into_iter().map(compute_total_fuel).sum();
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    let input : Vec<i64> = read_input(filename, "\n").expect("Error reading input");

    println!("Part 1: {}", part_one(&input));
    println!("Part 2: {}", part_two(&input));
}

#[cfg(test)]
mod tests {
    use super::{compute_fuel, compute_total_fuel};

    #[test]
    fn test_compute_fuel() {
        assert_eq!(compute_fuel(&12), 2);
        assert_eq!(compute_fuel(&14), 2);
        assert_eq!(compute_fuel(&1969), 654);
        assert_eq!(compute_fuel(&100756), 33583);

        assert_eq!(compute_fuel(&0), 0); // No negative fuel
    }
    #[test]
    fn test_compute_total_fuel() {
        assert_eq!(compute_total_fuel(&14), 2);
        assert_eq!(compute_total_fuel(&1969), 966);
        assert_eq!(compute_total_fuel(&100756), 50346);
    }
}
