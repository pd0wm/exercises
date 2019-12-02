use std::env;
use advent::read_input;

#[derive(Debug)]
struct ProgramState {
    halted: bool,
    pos: usize,
    values : Vec<i64>,
}

struct Arguments {
    a : i64,
    b : i64,
    result_location : usize,
}

fn get_arguments(state : &ProgramState) -> Arguments {
    let i_a = state.values[state.pos + 1] as usize;
    let i_b = state.values[state.pos + 2] as usize;

    let args = Arguments {
        a: state.values[i_a],
        b: state.values[i_b],
        result_location: state.values[state.pos + 3] as usize,
    };

    return args;
}


fn step(mut state : ProgramState) -> ProgramState {
    let instruction = state.values[state.pos];
    match instruction {
        1 => { // Add
            let args = get_arguments(&state);
            state.values[args.result_location] = args.a + args.b;
            state.pos += 4;
        }
        2 => { // Multiply
            let args = get_arguments(&state);
            state.values[args.result_location] = args.a * args.b;
            state.pos += 4;
        }
        99 => {
            state.halted = true;
        }
        _ => {}
    }

    return state;
}

fn run_till_halt(mut state : ProgramState) -> ProgramState {
    while !state.halted {
        state = step(state);
    }
    return state;
}

fn run_noun_verb(input : &Vec<i64>, noun : i64, verb : i64) -> i64{
    let mut state = ProgramState {halted: false, pos: 0, values: input.clone()};
    state.values[1] = noun;
    state.values[2] = verb;

    state = run_till_halt(state);

    return state.values[0];
}

fn part_one(input : &Vec<i64>) -> i64{
    return run_noun_verb(input, 12, 2);
}

fn part_two(input : &Vec<i64>) -> i64{
    for noun in 0..=99 {
        for verb in 0..=99 {
            if run_noun_verb(input, noun, verb) == 19690720{
                return 100 * noun + verb;
            }
        }
    }
    return -1;
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    let input : Vec<i64> = read_input(filename, ",").expect("Error reading input");

    println!("Part 1: {}", part_one(&input));
    println!("Part 2: {}", part_two(&input));
}


#[cfg(test)]
mod tests {
    use super::{ProgramState, step};

    #[test]
    fn test_add() {
        let start_state = ProgramState {halted: false, pos: 0, values: vec![1, 4, 5, 6, 3, 4, 0]};
        let end_state = step(start_state);

        assert_eq!(end_state.values[6], 7);
        assert_eq!(end_state.pos, 4);
        assert_eq!(end_state.halted, false);
    }

    #[test]
    fn test_multiply() {
        let start_state = ProgramState {halted: false, pos: 0, values: vec![2, 4, 5, 6, 3, 4, 0]};
        let end_state = step(start_state);

        assert_eq!(end_state.values[6], 12);
        assert_eq!(end_state.pos, 4);
        assert_eq!(end_state.halted, false);
    }

    #[test]
    fn test_halt() {
        let start_state = ProgramState {halted: false, pos: 0, values: vec![99]};
        let end_state = step(start_state);

        assert_eq!(end_state.halted, true);
    }
}
