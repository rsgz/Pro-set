#![allow(dead_code)]
#![allow(unused_variables)]

use std::collections::HashSet;
// 读数据
use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::path::Path;
// 写数据
use std::fs::OpenOptions;
use std::io::Write;

fn read_lines_from_file<P>(filename: P) -> io::Result<Vec<String>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let mut lines = Vec::new();
    for line in reader.lines() {
        let line = line?;
        // 可以选择在这里添加对网址格式的验证
        lines.push(line);
    }

    Ok(lines)
}

fn main() {
    let file_path = r"C:\Users\Administrator\Desktop\数据\类目网址3.txt";

    let urls = read_lines_from_file(file_path).unwrap();
    for (i, k) in urls.iter().enumerate() {
        if i % 10000 == 0 {
            // 每1000条记录打印一次
            println!("{}-->{}", i, k);
        }
    }
}
