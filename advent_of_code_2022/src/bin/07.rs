#![feature(test)]

use std::borrow::BorrowMut;
use std::cell::RefCell;
use std::ops::Deref;
use std::rc::{Rc, Weak};

extern crate test;

enum EntryType {
    File { size: usize },
    Directory { children: RefCell<Vec<Rc<Entry>>> },
}

struct Entry {
    name: String,
    typ: EntryType,
    parent: Weak<Entry>,
}

impl Entry {
    fn size(&self) -> usize {
        match &self.typ {
            EntryType::File { size } => *size,
            EntryType::Directory { children } => {
                children.borrow().deref().iter().map(|c| c.size()).sum()
            }
        }
    }
}

fn directories(entry: &Rc<Entry>) -> Vec<Rc<Entry>> {
    let mut ret = Vec::new();
    if let EntryType::Directory { children } = &entry.typ {
        ret.push(Rc::clone(&entry));
        for child in children.borrow().deref() {
            ret.append(&mut directories(&child));
        }
    };

    ret
}

fn part1(input: &Rc<Entry>) -> usize {
    directories(&input)
        .iter()
        .map(|d| d.size())
        .filter(|s| s < &100_000)
        .sum()
}

fn part2(input: &Rc<Entry>) -> usize {
    let available = 70_000_000 - input.size();

    directories(&input)
        .iter()
        .map(|d| d.size())
        .filter(|s| available + s > 3_0000_000)
        .min()
        .unwrap()
}

fn parse_input(input: &str) -> Rc<Entry> {
    let root = Rc::new(Entry {
        name: "/".to_string(),
        typ: EntryType::Directory {
            children: RefCell::new(Vec::new()),
        },
        parent: Weak::new(),
    });
    let mut cur = Rc::clone(&root);

    {
        for line in input.lines() {
            if line.starts_with("$ ls") {
                // Do nothing
            } else if line.starts_with("$ cd /") {
                cur = Rc::clone(&root);
            } else if line.starts_with("$ cd ..") {
                cur = cur.parent.upgrade().unwrap();
            } else if line.starts_with("$ cd") {
                if let &[_, _, dir_name] = &line.split(' ').collect::<Vec<&str>>()[..] {
                    if let EntryType::Directory { children } = &cur.clone().typ {
                        for child in children.borrow().deref() {
                            if child.name == dir_name {
                                cur = Rc::clone(&child);
                            }
                        }
                    }
                }
            } else if line.starts_with("dir") {
                // Dir
                if let &[_, dir_name] = &line.split(' ').collect::<Vec<&str>>()[..] {
                    let new_entry = Rc::new(Entry {
                        name: dir_name.to_string(),
                        typ: EntryType::Directory {
                            children: RefCell::new(Vec::new()),
                        },
                        parent: Rc::downgrade(&cur),
                    });
                    if let EntryType::Directory { children } = &cur.borrow_mut().typ {
                        children.borrow_mut().push(Rc::clone(&new_entry));
                    };
                }
            } else {
                // File
                if let &[size, filename] = &line.split(' ').collect::<Vec<&str>>()[..] {
                    let size: usize = size.parse().unwrap();
                    let new_entry = Rc::new(Entry {
                        name: filename.to_string(),
                        typ: EntryType::File { size },
                        parent: Rc::downgrade(&cur),
                    });
                    if let EntryType::Directory { children } = &cur.borrow_mut().typ {
                        children.borrow_mut().push(Rc::clone(&new_entry));
                    };
                }
            }
        }
    }
    root
}

fn main() {
    let values = parse_input(include_str!("../../inputs/07.txt").trim());
    println!("{}", part1(&values));
    println!("{}", part2(&values));
}

#[cfg(test)]
mod day07_tests {
    use super::*;
    use test::{black_box, Bencher};

    #[test]
    fn example() {
        let sample_input = parse_input(include_str!("../../inputs/07_sample.txt").trim());
        assert_eq!(95437, part1(&sample_input));
        assert_eq!(24933642, part2(&sample_input));
    }

    #[bench]
    fn bench_parsing(b: &mut Bencher) {
        b.iter(|| parse_input(include_str!("../../inputs/07.txt").trim()));
    }

    #[bench]
    fn bench_part1(b: &mut Bencher) {
        let values = black_box(parse_input(include_str!("../../inputs/07.txt").trim()));
        b.iter(|| part1(&values));
    }

    #[bench]
    fn bench_part2(b: &mut Bencher) {
        let values = black_box(parse_input(include_str!("../../inputs/07.txt").trim()));
        b.iter(|| part2(&values));
    }
}
