use image::codecs::jpeg::JpegDecoder;
// use image::DynamicImage;
// use std::io::Read;

use chrono::Local;
// use image::DynamicImage;
use image::{DynamicImage, GenericImageView, ImageBuffer, Rgba};
use rand::{seq::SliceRandom, thread_rng, Rng};
use rayon::prelude::*;
use std::collections::HashSet;
use std::fs;
// use std::io::Read;
use std::io::Read;
use std::path::{Path, PathBuf}; // 添加在文件开头的 use 语句中
                                // ========================= 画布宽高 ==============================
const TARGET_WIDTH: u32 = 1900;
const TARGET_HEIGHT: u32 = 600;
// ========================= 最多最少张 ==============================
// const MIN_IMAGES: usize = 4;
// const MAX_IMAGES: usize = 5;

const MIN_IMAGES: usize = 3;
const MAX_IMAGES: usize = 5;
// ========================= 要合成几张 ==============================
const BATCH_COUNT: usize = 30;

// 使用宏定义颜色
macro_rules! hex_color {
    ($hex:expr, $alpha:expr) => {
        [
            ($hex >> 16) as u8,
            (($hex >> 8) & 0xFF) as u8,
            ($hex & 0xFF) as u8,
            $alpha,
        ]
    };
}

// 渐变色定义
const GRADIENT_START: [u8; 4] = hex_color!(0x1bb5fd, 255);
const GRADIENT_END: [u8; 4] = hex_color!(0x3527fa, 255);

// 护眼模式配置
struct EyeProtectionConfig {
    warmth: f32,
    blue_reduction: f32,
    brightness: f32,
    contrast: f32,
    yellow_tint: f32,
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

struct ImageInfo {
    image: DynamicImage,
    width: u32,
    height: u32,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // ========================= 输入输出目录 ==============================
    let input_dir = r"E:\pic\pintu\2";
    let output_dir: &str = &format!("{}-2", input_dir);

    fs::create_dir_all(output_dir)?;
    process_batch(input_dir, output_dir)?;

    Ok(())
}
/*
fn process_batch(input_dir: &str, output_dir: &str) -> Result<(), Box<dyn std::error::Error>> {
    let image_paths: Vec<_> = fs::read_dir(input_dir)?
        .filter_map(|entry| entry.ok())
        .filter(|entry| {
            let path = entry.path();
            let ext = path.extension().and_then(|e| e.to_str()).unwrap_or("");
            matches!(ext.to_lowercase().as_str(), "jpg" | "jpeg" | "png" | "webp")
        })
        .map(|entry| entry.path())
        .collect();

    if image_paths.len() < MIN_IMAGES {
        println!("图片数量不够，至少需要 {} 张图片", MIN_IMAGES);
        return Ok(());
    }

    let mut used_images = HashSet::new();
    let mut rng = thread_rng();
    let config = EyeProtectionConfig::default();

    for batch_index in 0..BATCH_COUNT {
        let available_images: Vec<_> = image_paths
            .iter()
            .filter(|path| !used_images.contains(*path))
            .collect();

        if available_images.len() < MIN_IMAGES {
            println!("剩余图片数量不够，已完成 {} 张合成图", batch_index);
            break;
        }

        let max_attempts = 10;
        let mut attempt = 0;

        while attempt < max_attempts {
            let num_images = rng.gen_range(MIN_IMAGES..=MAX_IMAGES);
            let selected_paths: Vec<PathBuf> = available_images
                .choose_multiple(&mut rng, num_images)
                .map(|&p| p.clone())
                .collect();

            match create_combined_image(&selected_paths, &config) {
                Ok(final_image) => {
                    let now = Local::now();
                    let random_num = rng.gen_range(1000..9999);
                    let output_path = Path::new(output_dir).join(format!(
                        "combined_{}{:04}.png",
                        now.format("%Y%m%d_%H%M%S"),
                        random_num
                    ));

                    if let Ok(_) = final_image.save(&output_path) {
                        println!("成功保存: {}", output_path.display());

                        for path in &selected_paths {
                            // 删除本地图片
                            // if let Err(e) = fs::remove_file(path) {
                            //     println!("删除文件失败 {}: {}", path.display(), e);
                            // }
                            used_images.insert(path.clone());
                        }
                        break;
                    }
                }
                // Err(e) => {
                //     attempt += 1;
                //     if attempt >= max_attempts {
                //         println!("无法找到合适的图片组合: {}", e);
                //     }
                //     continue;
                // }
                Err(e) => println!("创建合成图失败: {}", e),
            }
        }
    }

    Ok(())
}
*/
fn process_batch(input_dir: &str, output_dir: &str) -> Result<(), Box<dyn std::error::Error>> {
    let image_paths: Vec<_> = fs::read_dir(input_dir)?
        .filter_map(|entry| entry.ok())
        .filter(|entry| {
            let path = entry.path();
            let ext = path.extension().and_then(|e| e.to_str()).unwrap_or("");
            matches!(ext.to_lowercase().as_str(), "jpg" | "jpeg" | "png" | "webp")
        })
        .map(|entry| entry.path())
        .collect();

    if image_paths.len() < MIN_IMAGES {
        println!("图片数量不够，至少需要 {} 张图片", MIN_IMAGES);
        return Ok(());
    }

    let mut used_images = HashSet::new();
    let mut rng = thread_rng();
    let config = EyeProtectionConfig::default();

    for _ in 0..BATCH_COUNT {
        let available_images: Vec<_> = image_paths
            .iter()
            .filter(|path| !used_images.contains(*path))
            .collect();

        if available_images.len() < MIN_IMAGES {
            println!("剩余图片数量不够，已完成合成");
            break;
        }

        let max_attempts = 10;
        let mut attempt = 0;

        while attempt < max_attempts {
            let num_images = rng.gen_range(MIN_IMAGES..=MAX_IMAGES);
            let selected_paths: Vec<PathBuf> = available_images
                .choose_multiple(&mut rng, num_images)
                .map(|&p| p.clone())
                .collect();

            match create_combined_image(&selected_paths, &config) {
                Ok(final_image) => {
                    let now = Local::now();
                    let random_num = rng.gen_range(1000..9999);
                    let output_path = Path::new(output_dir).join(format!(
                        "combined_{}{:04}.png",
                        now.format("%Y%m%d_%H%M%S"),
                        random_num
                    ));

                    if let Ok(_) = final_image.save(&output_path) {
                        println!("成功保存: {}", output_path.display());

                        for path in &selected_paths {
                            if let Err(e) = fs::remove_file(path) {
                                println!("删除文件失败 {}: {}", path.display(), e);
                            }
                            used_images.insert(path.clone());
                        }
                        break;
                    }
                }
                Err(e) => {
                    attempt += 1;
                    if attempt >= max_attempts {
                        println!("无法找到合适的图片组合: {}", e);
                    }
                    continue;
                }
            }
        }
    }

    Ok(())
}
// fn create_combined_image(
//     image_paths: &[PathBuf],
//     config: &EyeProtectionConfig,
// ) -> Result<ImageBuffer<Rgba<u8>, Vec<u8>>, Box<dyn std::error::Error>> {
//     let mut images: Vec<ImageInfo> = Vec::new();
//     let mut total_scaled_width = 0;

//     // 加载并处理每张图片
//     for path in image_paths {
//         let img = match detect_image_format(path)? {
//             image::ImageFormat::Jpeg => image::open(path)?,
//             image::ImageFormat::Png => image::open(path)?,
//             image::ImageFormat::WebP => image::open(path)?,
//             _ => return Err("Unsupported image format".into()),
//         };

//         let aspect_ratio = img.width() as f32 / img.height() as f32;
//         let scaled_width = (TARGET_HEIGHT as f32 * aspect_ratio) as u32;

//         images.push(ImageInfo {
//             image: img,
//             width: scaled_width,
//             height: TARGET_HEIGHT,
//         });

//         total_scaled_width += scaled_width;
//     }
// 修改 create_combined_image 函数中的图片加载部分
// fn create_combined_image(
//     image_paths: &[PathBuf],
//     config: &EyeProtectionConfig,
// ) -> Result<ImageBuffer<Rgba<u8>, Vec<u8>>, Box<dyn std::error::Error>> {
//     let mut images: Vec<ImageInfo> = Vec::new();
//     let mut total_scaled_width = 0;

//     // 加载并处理每张图片
//     for path in image_paths {
//         // 直接使用 image::open 而不进行格式检测
//         let img =
//             image::open(path).map_err(|e| format!("Failed to open image {:?}: {}", path, e))?;

//         let aspect_ratio = img.width() as f32 / img.height() as f32;
//         let scaled_width = (TARGET_HEIGHT as f32 * aspect_ratio) as u32;

//         images.push(ImageInfo {
//             image: img,
//             width: scaled_width,
//             height: TARGET_HEIGHT,
//         });

//         total_scaled_width += scaled_width;
//     }
/*
[0xFF, 0xD8, 0xFF, 0xE1] 是 JPEG 文件的标准文件头（magic numbers），这说明这个文件虽然扩展名是 .webp，但实际上是一个 JPEG 文件。
*/

// 修改 create_combined_image 函数中的相关代码
fn create_combined_image(
    image_paths: &[PathBuf],
    config: &EyeProtectionConfig,
) -> Result<ImageBuffer<Rgba<u8>, Vec<u8>>, Box<dyn std::error::Error>> {
    let mut images: Vec<ImageInfo> = Vec::new();
    let mut total_scaled_width = 0;

    for path in image_paths {
        // 读取文件头来判断真实格式
        let mut file = std::fs::File::open(path)?;
        let mut buffer = [0; 16];
        file.read_exact(&mut buffer)?;

        // 检查文件头
        let is_jpeg = buffer.starts_with(&[0xFF, 0xD8, 0xFF]);

        // 重新打开文件并根据实际格式处理
        let img = if is_jpeg {
            JpegDecoder::new(std::fs::File::open(path)?)
                .map_err(|e| format!("JPEG decode error: {}", e))
                .and_then(|decoder| {
                    DynamicImage::from_decoder(decoder)
                        .map_err(|e| format!("Failed to create image: {}", e))
                })?
        } else {
            // 尝试常规打开
            image::open(path).map_err(|e| format!("Failed to open image {:?}: {}", path, e))?
        };

        let aspect_ratio = img.width() as f32 / img.height() as f32;
        let scaled_width = (TARGET_HEIGHT as f32 * aspect_ratio) as u32;

        images.push(ImageInfo {
            image: img,
            width: scaled_width,
            height: TARGET_HEIGHT,
        });

        total_scaled_width += scaled_width;
    }
    // 验证组合是否合适
    if !validate_image_combination(&images) {
        return Err("Images combination cannot cover the target width".into());
    }

    let mut final_image = ImageBuffer::new(TARGET_WIDTH, TARGET_HEIGHT);

    // 填充白色背景
    for pixel in final_image.pixels_mut() {
        *pixel = Rgba([255, 255, 255, 255]);
    }

    // 计算重叠量
    let total_overlap = if total_scaled_width > TARGET_WIDTH {
        (total_scaled_width - TARGET_WIDTH) / (images.len() - 1) as u32
    } else {
        0
    };

    // 绘制图片
    let mut x_offset = 0;
    for (i, img_info) in images.iter().enumerate() {
        let resized = img_info.image.resize(
            img_info.width,
            img_info.height,
            image::imageops::FilterType::Lanczos3,
        );

        let overlap = if i < images.len() - 1 {
            total_overlap
        } else {
            0
        };

        image::imageops::overlay(&mut final_image, &resized, x_offset as i64, 0);

        x_offset += img_info.width - overlap;
    }

    // 添加渐变效果
    apply_gradient(&mut final_image);

    // 应用护眼模式
    apply_eye_protection(&mut final_image, config);

    Ok(final_image)
}

// 检测图片格式
// fn detect_image_format(path: &Path) -> Result<image::ImageFormat, Box<dyn std::error::Error>> {
//     let file = std::fs::File::open(path)?;
//     let reader = std::io::BufReader::new(file);
//     let format = image::guess_format(reader.buffer())?;
//     Ok(format)
// }

// 修改 detect_image_format 函数
fn detect_image_format(path: &Path) -> Result<image::ImageFormat, Box<dyn std::error::Error>> {
    let file = std::fs::File::open(path)?;
    let mut reader = std::io::BufReader::new(file);
    let mut buffer = [0; 16];
    reader.read_exact(&mut buffer)?;
    let format = image::guess_format(&buffer)?;
    Ok(format)
}

// 验证图片组合是否合适
// fn validate_image_combination(images: &[ImageInfo]) -> bool {
//     let mut total_width = 0;
//     for img in images {
//         total_width += img.width;
//     }

//     // 计算重叠后的总宽度
//     if images.len() > 1 {
//         let total_overlap = (total_width - TARGET_WIDTH) / (images.len() - 1) as u32;
//         total_width -= total_overlap * (images.len() - 1) as u32;
//     }

//     // 确保覆盖至少98%的目标宽度
//     total_width >= (TARGET_WIDTH as f32 * 0.98) as u32
// }
// 溢出错误的修复
fn validate_image_combination(images: &[ImageInfo]) -> bool {
    let mut total_width: u32 = 0;

    // 防止溢出的安全检查
    for img in images {
        // 检查是否会溢出
        if let Some(new_width) = total_width.checked_add(img.width) {
            total_width = new_width;
        } else {
            return false; // 宽度溢出，组合无效
        }
    }

    // 计算重叠后的总宽度
    if images.len() > 1 {
        let overlap = if let Some(width_diff) = total_width.checked_sub(TARGET_WIDTH) {
            width_diff / (images.len() - 1) as u32
        } else {
            return false; // 宽度差异计算溢出
        };

        // 计算重叠后的实际宽度
        if let Some(overlap_total) = overlap.checked_mul((images.len() - 1) as u32) {
            if let Some(final_width) = total_width.checked_sub(overlap_total) {
                total_width = final_width;
            } else {
                return false;
            }
        } else {
            return false;
        }
    }

    // 确保覆盖至少98%的目标宽度
    total_width >= (TARGET_WIDTH as f32 * 0.98) as u32
}

// 应用渐变效果
fn apply_gradient(image: &mut ImageBuffer<Rgba<u8>, Vec<u8>>) {
    let width = image.width();
    let height = image.height();

    for y in 0..height {
        for x in 0..width {
            // 计算渐变进度 (左下到右上)
            let progress = (x as f32 / width as f32 + (height - y) as f32 / height as f32) / 2.0;

            // 计算渐变颜色
            let gradient_color = interpolate_color(&GRADIENT_START, &GRADIENT_END, progress);

            // 获取原始像素
            let pixel = image.get_pixel_mut(x, y);
            let original = pixel.0;

            // 应用正片叠底混合
            *pixel = multiply_blend(&Rgba(original), &gradient_color);
        }
    }
}

// 颜色插值
fn interpolate_color(start: &[u8; 4], end: &[u8; 4], t: f32) -> Rgba<u8> {
    let r = (start[0] as f32 * (1.0 - t) + end[0] as f32 * t) as u8;
    let g = (start[1] as f32 * (1.0 - t) + end[1] as f32 * t) as u8;
    let b = (start[2] as f32 * (1.0 - t) + end[2] as f32 * t) as u8;
    let a = (start[3] as f32 * (1.0 - t) + end[3] as f32 * t) as u8;
    Rgba([r, g, b, a])
}

// 正片叠底混合
fn multiply_blend(bottom: &Rgba<u8>, top: &Rgba<u8>) -> Rgba<u8> {
    let b = bottom.0;
    let t = top.0;

    Rgba([
        ((b[0] as f32 * t[0] as f32) / 255.0) as u8,
        ((b[1] as f32 * t[1] as f32) / 255.0) as u8,
        ((b[2] as f32 * t[2] as f32) / 255.0) as u8,
        ((b[3] as f32 * t[3] as f32) / 255.0) as u8,
    ])
}

// 应用护眼模式
fn apply_eye_protection(image: &mut ImageBuffer<Rgba<u8>, Vec<u8>>, config: &EyeProtectionConfig) {
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

// 获取目录中的所有图片文件
// fn get_image_files<P: AsRef<Path>>(dir: P) -> Vec<PathBuf> {
//     let supported_formats = vec!["jpg", "jpeg", "png", "webp"];

//     fs::read_dir(dir)
//         .expect("无法读取目录")
//         .filter_map(|entry| entry.ok())
//         .filter(|entry| {
//             if let Some(extension) = entry.path().extension() {
//                 if let Some(ext) = extension.to_str() {
//                     return supported_formats.contains(&ext.to_lowercase().as_str());
//                 }
//             }
//             false
//         })
//         .map(|entry| entry.path())
//         .collect()
// }

fn get_image_files<P: AsRef<Path>>(dir: P) -> Vec<PathBuf> {
    let supported_formats = vec!["jpg", "jpeg", "png", "webp"];

    fs::read_dir(dir)
        .expect("无法读取目录")
        .filter_map(|entry| {
            let entry = entry.ok()?;
            let path = entry.path();

            // 尝试打开文件并读取文件头
            if let Ok(mut file) = std::fs::File::open(&path) {
                let mut buffer = [0; 16];
                if file.read_exact(&mut buffer).is_ok() {
                    // 检查是否为 JPEG
                    if buffer.starts_with(&[0xFF, 0xD8, 0xFF]) {
                        return Some(path);
                    }

                    // 检查是否为 PNG
                    if buffer.starts_with(&[0x89, 0x50, 0x4E, 0x47]) {
                        return Some(path);
                    }

                    // 检查是否为 WebP
                    if buffer.starts_with(b"RIFF") && buffer[8..12] == *b"WEBP" {
                        return Some(path);
                    }
                }
            }

            // 如果无法通过文件头判断，则通过扩展名判断
            if let Some(extension) = path.extension() {
                if let Some(ext) = extension.to_str() {
                    if supported_formats.contains(&ext.to_lowercase().as_str()) {
                        return Some(path);
                    }
                }
            }
            None
        })
        .collect()
}
