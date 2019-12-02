use std::io;
use std::io::BufRead;
use std::fs::File;
use std::str::FromStr;
use std::error::Error;

pub fn read_input<T>(filename : &str) -> io::Result<Vec<T>>
where T: FromStr, T::Err: 'static + Error + Send + Sync
{
    let mut r = Vec::new();

    let file = File::open(filename)?;
    let br = io::BufReader::new(file);

    for line in br.lines() {
        let line = line?;
        let n = line.parse().map_err(|e| io::Error::new(io::ErrorKind::InvalidData, e))?;
        r.push(n);
    }

    return Ok(r);
}
