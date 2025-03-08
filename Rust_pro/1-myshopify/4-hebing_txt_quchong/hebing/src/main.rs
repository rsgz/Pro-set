#![allow(unused_imports)]
#![allow(path_statements)]
#![allow(unused_variables)]
#![allow(unused_mut)]
#![allow(unused_must_use)]

use std::collections::HashSet; // 去重
use std::fs; // 获取目录
use std::fs::File;
use std::fs::OpenOptions;
use std::io::{self, BufRead, BufReader, Write};
use std::path::Path;

// 从文件中读取所有行
pub fn get_lines<P>(filename: P) -> io::Result<Vec<String>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let mut lines = Vec::new();
    for line in reader.lines() {
        lines.push(line?);
    }
    Ok(lines)
}

fn main() -> io::Result<()> {
    let dir_path = r"C:\Users\Administrator\Desktop\数据\yuming";
    let dir_entries = fs::read_dir(dir_path)?;

    let mut all_lines_set: HashSet<String> = HashSet::new(); // 用于全局去重

    // 遍历目录中的每个文件
    for dir_entry in dir_entries {
        let entry = dir_entry?;
        let file_path = entry.path();

        if file_path.is_file() {
            println!("Processing file: {:?}", file_path);

            // 读取文件的所有行
            let lines = match get_lines(&file_path) {
                Ok(lines) => lines,
                Err(e) => {
                    eprintln!("Error reading file {:?}: {}", file_path, e);
                    continue;
                }
            };

            // 将文件中的行添加到全局去重集合中
            all_lines_set.extend(lines);
        }
    }

    // 将去重后的行保存到目标文件
    let file_path = r"C:\Users\Administrator\Desktop\数据\yuming\yuming_all3.txt";
    let mut file = OpenOptions::new()
        .create(true)
        .append(true)
        .open(file_path)?;

    for (i, line) in all_lines_set.into_iter().enumerate() {
        if i % 10000 == 0 {
            println!("Writing line {}: {}", i, line);
        }
        writeln!(file, "{}", line)?;
    }

    Ok(())
}
