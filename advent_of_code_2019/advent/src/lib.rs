use std::fs;
use std::str::FromStr;
use std::error::Error;
use std::str;

pub fn read_input<T>(filename : &str, sep : &str) -> Result<Vec<T>, Box<dyn Error>>
where T: FromStr, T::Err: 'static + Error + Send + Sync
{
    let mut r = Vec::new();

    let contents = fs::read_to_string(filename)?;

    for val in contents.split(sep) {
        let val = val.trim();
        if val.len() > 0 {
            r.push(val.parse()?);
        }
    }

    return Ok(r);
}
