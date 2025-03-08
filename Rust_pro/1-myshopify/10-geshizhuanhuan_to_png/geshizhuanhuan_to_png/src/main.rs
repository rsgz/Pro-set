use image::ImageFormat;
use rayon::prelude::*;
use std::fs;
use std::path::{Path, PathBuf};

fn main() {
    // 指定源目录和目标目录
    let source_dir = r"E:\pic\600-370\Hoodies"; // 源图片目录

    let output_dir = r"E:\pic\600-370\Hoodies2"; // 输出PNG图片目录

    // 创建输出目录（如果不存在）
    fs::create_dir_all(output_dir).expect("无法创建输出目录");

    // 获取所有支持的图片文件
    let image_files: Vec<PathBuf> = get_image_files(source_dir);
    let total_files = image_files.len();
    println!("找到 {} 个图片文件", total_files);

    // 并行处理所有图片
    let results: Vec<_> = image_files
        .par_iter()
        .map(|path| match convert_to_png(path, output_dir) {
            Ok(_) => {
                println!("成功转换: {:?}", path.file_name().unwrap());
                true
            }
            Err(e) => {
                println!("转换失败 {:?}: {}", path.file_name().unwrap(), e);
                false
            }
        })
        .collect();

    // 统计结果
    let success_count = results.iter().filter(|&&success| success).count();
    let fail_count = total_files - success_count;

    println!("\n转换完成!");
    println!("成功: {} 个文件", success_count);
    println!("失败: {} 个文件", fail_count);
}

// 获取目录中的所有图片文件
fn get_image_files<P: AsRef<Path>>(dir: P) -> Vec<PathBuf> {
    let supported_formats = vec!["jpg", "jpeg", "bmp", "gif", "tiff", "webp"];

    fs::read_dir(dir)
        .expect("无法读取目录")
        .filter_map(|entry| entry.ok())
        .filter(|entry| {
            if let Some(extension) = entry.path().extension() {
                if let Some(ext) = extension.to_str() {
                    return supported_formats.contains(&ext.to_lowercase().as_str());
                }
            }
            false
        })
        .map(|entry| entry.path())
        .collect()
}

// 将单个图片转换为PNG
fn convert_to_png(source_path: &Path, output_dir: &str) -> Result<(), String> {
    // 读取图片
    let img = image::open(source_path).map_err(|e| format!("无法打开图片: {}", e))?;

    // 创建输出文件路径
    let file_stem = source_path
        .file_stem()
        .and_then(|s| s.to_str())
        .ok_or("无法获取文件名")?;

    let output_path = Path::new(output_dir).join(format!("{}.png", file_stem));

    // 保存为PNG
    img.save_with_format(&output_path, ImageFormat::Png)
        .map_err(|e| format!("无法保存PNG: {}", e))?;

    Ok(())
}
