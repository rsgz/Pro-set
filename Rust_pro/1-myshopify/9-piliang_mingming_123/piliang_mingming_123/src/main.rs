use std::collections::HashMap;
use std::fs;
use std::io;
use std::path::Path;

fn main() -> io::Result<()> {
    // ------------------------------------------------------------->
    let dir_path = r"E:\pic\600-400\Mini Dresses2";

    // 支持的图片格式
    let image_extensions: Vec<&str> = vec!["jpg", "jpeg", "png", "gif", "bmp", "webp"];

    // 获取并排序文件
    let mut paths: Vec<_> = fs::read_dir(dir_path)?
        .filter_map(|entry| entry.ok())
        .filter(|entry| {
            if let Some(extension) = entry.path().extension() {
                if let Some(ext) = extension.to_str() {
                    return image_extensions.contains(&ext.to_lowercase().as_str());
                }
            }
            false
        })
        .collect();

    // 按文件名排序
    paths.sort_by(|a, b| a.file_name().cmp(&b.file_name()));

    println!("找到 {} 个图片文件", paths.len());

    // 统计文件类型
    let mut extension_count: HashMap<String, i32> = HashMap::new();

    // 遍历重命名
    for (index, entry) in paths.iter().enumerate() {
        let old_path = entry.path();

        // 获取扩展名
        let extension = old_path
            .extension()
            .and_then(|ext| ext.to_str())
            .unwrap_or("")
            .to_lowercase();

        // 统计文件类型
        *extension_count.entry(extension.clone()).or_insert(0) += 1;

        // 构建新文件名 (保持原扩展名)
        let new_name = format!("{}.{}", index + 1, extension);
        let new_path = Path::new(dir_path).join(&new_name);

        // 检查新文件名是否已存在
        if new_path.exists() {
            println!("警告: {} 已存在，跳过", new_name);
            continue;
        }

        // 执行重命名
        println!(
            "重命名: {:?} -> {}",
            old_path.file_name().unwrap(),
            new_name
        );
        fs::rename(old_path, new_path)?;
    }

    // 打印统计信息
    println!("\n文件类型统计:");
    for (ext, count) in extension_count.iter() {
        println!("{}: {} 个文件", ext, count);
    }

    println!("\n重命名完成！共处理 {} 个文件", paths.len());
    Ok(())
}
