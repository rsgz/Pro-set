use std::fs::File;
use std::io::{self, BufRead, BufReader, Write};
// use std::path::Path;

fn main() -> io::Result<()> {
    // 配置参数
    // let input_path = r"C:\Users\Administrator\Desktop\数据\0-女2.txt"; // 输入文件名
    let input_path = r"C:\Users\Administrator\Desktop\rust_url3.txt"; // 输入文件名
    let lines_per_file = 5000; // 每个文件的行数
    let output_prefix = "output_part_"; // 输出文件的前缀

    // 打开输入文件
    let file = File::open(input_path)?;
    let reader = BufReader::new(file);

    let mut current_file_number = 1;
    let mut current_line_count = 0;
    let mut current_writer: Option<File> = None;

    // 逐行读取并写入
    for line in reader.lines() {
        let line = line?;

        // 如果需要创建新文件
        if current_line_count % lines_per_file == 0 {
            // 创建新的输出文件
            let output_filename = format!(
                r"C:\Users\Administrator\Desktop\数据\5000\{}{}.txt",
                output_prefix, current_file_number
            );
            println!("Creating new file: {}", output_filename);

            current_writer = Some(File::create(output_filename)?);
            current_file_number += 1;
        }

        // 写入当前行
        if let Some(ref mut writer) = current_writer {
            writeln!(writer, "{}", line)?;
        }

        current_line_count += 1;
    }

    println!("切割完成! 创建了 {} 文件!", current_file_number - 1);
    Ok(())
}
