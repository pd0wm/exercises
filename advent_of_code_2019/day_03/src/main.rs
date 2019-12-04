use std::env;
use std::fs;
use std::collections::HashSet;
use std::collections::HashMap;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];

    let contents = fs::read_to_string(filename).expect("Error reading input");

    let mut lines : Vec<HashSet<(i64, i64)>> = Vec::new();
    let mut lines_steps : Vec<HashMap<(i64, i64), i64>> = Vec::new();

    for line in contents.split("\n") {
        if line.len() == 0 {
            continue;
        }

        let mut positions = HashSet::new();
        let mut steps = HashMap::new();

        let mut x = 0;
        let mut y = 0;
        let mut i = 0;

        for command in line.split(",") {
            let direction = &command[0..1];
            let amount : i64 = command[1..].parse().unwrap();

            for _ in 0..amount {
                match direction {
                    "R" => x += 1,
                    "U" => y += 1,
                    "D" => y -= 1,
                    "L" => x -= 1,
                    _ => {},
                }
                i += 1;

                positions.insert((x, y));
                steps.insert((x, y), i);
            }

        }

        lines.push(positions);
        lines_steps.push(steps);
    }

    let intersections = lines[0].intersection(&lines[1]);
    let closest = intersections.clone().map(|i| i.0.abs() + i.1.abs()).min().unwrap();
    println!("Part 1: {}", closest);

    let num_steps = intersections.clone().map(|i| lines_steps[0].get(i).unwrap() + lines_steps[1].get(i).unwrap() ).min().unwrap();
    println!("Part 2: {}", num_steps);


}
