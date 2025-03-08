use std::fs::File;
use std::io::{self, BufRead, BufReader, Write};

fn main() -> io::Result<()> {
    // 打开输入文件
    let input_file = File::open(r"C:\Users\Administrator\Desktop\数据\类目网址2.txt")?;
    let reader = BufReader::new(input_file);

    // 创建输出文件
    let mut output_file = File::create(r"C:\Users\Administrator\Desktop\数据\类目网址3.txt")?;

    // 逐行处理
    for line in reader.lines() {
        let line = line?;
        if let Some(index) = line.find("https://") {
            // 只保留 https:// 及其右边的内容
            let result = &line[index..];
            writeln!(output_file, "{}", result)?;
        }
    }

    Ok(())
}
