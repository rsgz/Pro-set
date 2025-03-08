use image::{ImageBuffer, Rgba, RgbaImage};
use rayon::prelude::*;
use std::fs;
// use std::path::PathBuf;
use std::path::{Path, PathBuf};

// 护眼模式配置
/*
可以通过调整 EyeProtectionConfig 中的参数来自定义护眼效果：
warmth: 暖色调强度
blue_reduction: 蓝光降低程度
brightness: 整体亮度
contrast: 对比度
yellow_tint: 黄色色调强度
 */
struct EyeProtectionConfig {
    warmth: f32,         // 暖色调强度 (0.0 - 1.0)
    blue_reduction: f32, // 蓝光降低程度 (0.0 - 1.0)
    brightness: f32,     // 整体亮度 (0.0 - 1.0)
    contrast: f32,       // 对比度调整 (0.0 - 2.0)
    yellow_tint: f32,    // 黄色色调强度 (0.0 - 1.0)
}

impl Default for EyeProtectionConfig {
    fn default() -> Self {
        Self {
            warmth: 0.3,
            blue_reduction: 0.2,
            brightness: 0.95,
            contrast: 1.0,
            yellow_tint: 0.1,
        }
    }
}

fn main() {
    // let input_dir = r"E:\pic\sp\600-400-32"; // 输入图片目录  // --> &str
    let input_dir = r"E:\pic\sp\600-400-32"; // 输入图片目录  // --> &str
    let output_dir: &str = &format!("{}2", input_dir); // --> &str

    // 创建输出目录
    fs::create_dir_all(output_dir).expect("无法创建输出目录");

    // 获取所有图片文件
    let image_files = get_image_files(input_dir);
    println!("找到 {} 个图片文件", image_files.len());

    // 获取护眼模式配置
    let config = EyeProtectionConfig::default();

    // 并行处理图片
    image_files
        .par_iter()
        .for_each(|path| match process_image(path, output_dir, &config) {
            Ok(_) => println!("成功处理: {:?}", path.file_name().unwrap()),
            Err(e) => println!("处理失败 {:?}: {}", path.file_name().unwrap(), e),
        });
}

fn process_image(
    input_path: &Path,
    output_dir: &str,
    config: &EyeProtectionConfig,
) -> Result<(), String> {
    // 读取原始图片
    let mut img = image::open(input_path)
        .map_err(|e| format!("无法打开图片: {}", e))?
        .into_rgba8();

    // 应用护眼模式
    apply_eye_protection(&mut img, config);

    // 保存结果
    let file_name = input_path
        .file_stem()
        .and_then(|s| s.to_str())
        .ok_or("无法获取文件名")?;

    let output_path = Path::new(output_dir).join(format!("{}.png", file_name));

    img.save(output_path)
        .map_err(|e| format!("无法保存图片: {}", e))?;

    Ok(())
}

fn apply_eye_protection(image: &mut RgbaImage, config: &EyeProtectionConfig) {
    for pixel in image.pixels_mut() {
        let mut r = pixel[0] as f32;
        let mut g = pixel[1] as f32;
        let mut b = pixel[2] as f32;
        let a = pixel[3];

        // 1. 应用对比度
        r = ((r / 255.0 - 0.5) * config.contrast + 0.5) * 255.0;
        g = ((g / 255.0 - 0.5) * config.contrast + 0.5) * 255.0;
        b = ((b / 255.0 - 0.5) * config.contrast + 0.5) * 255.0;

        // 2. 增加暖色调
        r = r * (1.0 + config.warmth);
        g = g * (1.0 + config.warmth * 0.5);

        // 3. 降低蓝光
        b = b * (1.0 - config.blue_reduction);

        // 4. 添加黄色色调
        r = r * (1.0 + config.yellow_tint);
        g = g * (1.0 + config.yellow_tint);

        // 5. 调整整体亮度
        r *= config.brightness;
        g *= config.brightness;
        b *= config.brightness;

        // 确保值在 0-255 范围内
        r = r.min(255.0).max(0.0);
        g = g.min(255.0).max(0.0);
        b = b.min(255.0).max(0.0);

        // 更新像素值
        *pixel = Rgba([r as u8, g as u8, b as u8, a]);
    }
}

fn get_image_files<P: AsRef<Path>>(dir: P) -> Vec<PathBuf> {
    let supported_formats = vec!["jpg", "jpeg", "png", "gif", "bmp", "webp"];

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
