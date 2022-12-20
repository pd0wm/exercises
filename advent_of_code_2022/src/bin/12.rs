#![feature(test)]
#![feature(let_chains)]

use petgraph::algo::dijkstra;
use petgraph::graph::{Graph, NodeIndex};

extern crate test;

type Input = (Graph<u8, ()>, NodeIndex, NodeIndex);

fn part1(input: &Input) -> i32 {
    *dijkstra(&input.0, input.2, Some(input.1), |_| 1)
        .get(&input.1)
        .unwrap()
}

fn part2(input: &Input) -> i32 {
    let paths = dijkstra(&input.0, input.2, None, |_| 1);
    let starts = input
        .0
        .node_indices()
        .filter(|i| input.0.node_weight(*i).unwrap() == &height('a'));
    *starts
        .map(|s| paths.get(&s).unwrap_or(&i32::MAX))
        .min()
        .unwrap()
}

fn height(c: char) -> u8 {
    match c {
        'S' => height('a'),
        'E' => height('z'),
        c => c as u8,
    }
}

fn connects(from: char, to: char) -> bool {
    height(from) + 1 >= height(to)
}

fn get(input: &Vec<Vec<char>>, x: isize, y: isize) -> Option<char> {
    let h = input.len() as isize;
    let w = input[0].len() as isize;

    if x >= 0 && x < w && y >= 0 && y < h {
        Some(input[y as usize][x as usize])
    } else {
        None
    }
}

fn parse_input(input: &str) -> Input {
    let input: Vec<Vec<char>> = input.lines().map(|l| l.chars().collect()).collect();
    let mut graph = Graph::new();

    let h = input.len() as isize;
    let w = input[0].len() as isize;

    let nodes: Vec<Vec<NodeIndex>> = (0..h)
        .map(|y| {
            (0..w)
                .map(|x| graph.add_node(height(get(&input, x, y).unwrap())))
                .collect()
        })
        .collect();

    let mut start: Option<NodeIndex> = None;
    let mut end: Option<NodeIndex> = None;

    for y in 0..h {
        for x in 0..w {
            if input[y as usize][x as usize] == 'S' {
                start = Some(nodes[y as usize][x as usize]);
            }
            if input[y as usize][x as usize] == 'E' {
                end = Some(nodes[y as usize][x as usize]);
            }

            let from = get(&input, x, y).unwrap();

            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
                if let Some(to) = get(&input, x + dx, y + dy) && connects(from, to) {
                    // Add edge backwards since we're looking from end to start
                    graph.add_edge(nodes[(y + dy) as usize][(x + dx) as usize], nodes[y as usize][x as usize], ());
                }
            }
        }
    }

    (graph, start.unwrap(), end.unwrap())
}

fn main() {
    let values = parse_input(include_str!("../../inputs/12.txt").trim());
    println!("{}", part1(&values));
    println!("{}", part2(&values));
}

#[cfg(test)]
mod day12_tests {
    use super::*;
    use test::{black_box, Bencher};

    #[test]
    fn example() {
        let sample_input = parse_input(include_str!("../../inputs/12_sample.txt").trim());
        assert_eq!(31, part1(&sample_input));
        assert_eq!(29, part2(&sample_input));
    }
    #[test]
    fn test_connects() {
        assert_eq!(true, connects('a', 'b'));
        assert_eq!(true, connects('a', 'a'));
        assert_eq!(true, connects('z', 'a'));
        assert_eq!(true, connects('b', 'a'));
        assert_eq!(false, connects('a', 'c'));
    }

    #[bench]
    fn bench_parsing(b: &mut Bencher) {
        b.iter(|| parse_input(include_str!("../../inputs/12.txt").trim()));
    }

    #[bench]
    fn bench_part1(b: &mut Bencher) {
        let values = black_box(parse_input(include_str!("../../inputs/12.txt").trim()));
        b.iter(|| part1(&values));
    }

    #[bench]
    fn bench_part2(b: &mut Bencher) {
        let values = black_box(parse_input(include_str!("../../inputs/12.txt").trim()));
        b.iter(|| part2(&values));
    }
}
