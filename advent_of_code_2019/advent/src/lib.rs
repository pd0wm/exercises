use std::error::Error;
use std::io::{BufRead, BufReader};
use std::fs::File;

pub fn read_input(filename : &String) -> Result<Vec<i64>, Box<dyn Error>> {
    let mut r = Vec::new();

    let file = File::open(filename)?;
    let br = BufReader::new(file);

    for line in br.lines() {
        let line = line?;
        let n = line.parse()?;
        r.push(n);
    }

    return Ok(r);
}
