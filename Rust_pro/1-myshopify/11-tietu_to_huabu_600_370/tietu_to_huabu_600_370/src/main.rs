use image::{imageops, GenericImageView, ImageBuffer, Rgba, RgbaImage};
use rayon::prelude::*;
use rusttype::{Font, Scale};
use std::fs;
use std::path::{Path, PathBuf};

// 画布尺寸 ----------------------画布尺寸------------------->
const CANVAS_WIDTH: u32 = 600;
// const CANVAS_HEIGHT: u32 = 320;
const CANVAS_HEIGHT: u32 = 700;

// 渐变色起始和结束颜色  这第一个版本 修改颜色太麻烦了
// const GRADIENT_START: [u8; 4] = [0x00, 0xAE, 0xFF, 0xFF]; // #00aeff
// const GRADIENT_END: [u8; 4] = [0x1F, 0x0F, 0xF8, 0xFF]; // #1f0ff8

// 使用方式：  忘记了在常量中的限制。对于常量定义，使用宏是更好的选择：
// const GRADIENT_START: [u8; 4] = hex_to_rgba("#00aeff", 255);
// const GRADIENT_END: [u8; 4] = hex_to_rgba("#1f0ff8", 255);

// 定义一个宏来处理十六进制颜色
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

// 使用宏定义颜色常量--------------------------颜色------------------------------>
// 颜色代码从 #00aeff 改写为 0x00aeff 即可。  宏不能直接处理 # 开头的十六进制字符串  使用 0x 前缀
// const GRADIENT_START: [u8; 4] = hex_color!(0x1bb5fd, 255);
// const GRADIENT_END: [u8; 4] = hex_color!(0x3527fa, 255);

const GRADIENT_START: [u8; 4] = hex_color!(0xf9cbeb, 255);
const GRADIENT_END: [u8; 4] = hex_color!(0xbe70a7, 255);

// --------------------------字体尺寸------------------------------>
const ziti_chicun: f32 = 140.0; // 字体尺寸  一定要180.0  小数点少了就会报错  Mini Dresses 300*200
                                // const ziti_chicun: f32 = 160.0; // 字体尺寸  一定要180.0  小数点少了就会报错  Mini Dresses 600*600
                                // const ziti_chicun: f32 = 180.0; // 字体尺寸  一定要180.0  小数点少了就会报错 600*370  Swimsuit 600*800
                                // const ziti_chicun: f32 = 200.0; // 字体尺寸  一定要180.0  小数点少了就会报错  600-750\Skirt
static shuiyin: &str = " ";
// static shuiyin: &str = "T-Shirts";

fn main() {
    // --------------------------输入输出目录------------------------------>
    // let input_dir = r"E:\pic\sp\600-400-3"; // 输入图片目录
    let input_dir = r"E:\pic\sp\0"; // 输入图片目录
                                    // let output_dir = r"E:\pic\600-600\Mini Dresses"; // 输出图片目录
    let output_dir: &str = &format!("{}2", input_dir); // -->&str

    // 创建输出目录
    fs::create_dir_all(output_dir).expect("无法创建输出目录");

    // 获取所有图片文件
    let image_files = get_image_files(input_dir);
    println!("找到 {} 个图片文件", image_files.len());

    // 并行处理图片
    image_files
        .par_iter()
        .for_each(|path| match process_image(path, output_dir) {
            Ok(_) => println!("成功处理: {:?}", path.file_name().unwrap()),
            Err(e) => println!("处理失败 {:?}: {}", path.file_name().unwrap(), e),
        });
}

// 方法1：直接转换十六进制字符串
fn hex_to_rgba(hex: &str, alpha: u8) -> [u8; 4] {
    let hex = hex.trim_start_matches('#');
    [
        u8::from_str_radix(&hex[0..2], 16).unwrap_or(0),
        u8::from_str_radix(&hex[2..4], 16).unwrap_or(0),
        u8::from_str_radix(&hex[4..6], 16).unwrap_or(0),
        alpha,
    ]
}

//
fn process_image(input_path: &Path, output_dir: &str) -> Result<(), String> {
    // 创建空白画布
    let mut canvas = RgbaImage::new(CANVAS_WIDTH, CANVAS_HEIGHT);

    // 填充白色背景 (R=255, G=255, B=255, A=255)
    for pixel in canvas.pixels_mut() {
        *pixel = Rgba([255, 255, 255, 255]);
    }

    // 读取原始图片
    let img = image::open(input_path).map_err(|e| format!("无法打开图片: {}", e))?;

    // 计算等比例缩放后的尺寸
    let (width, height) = calculate_dimensions(img.width(), img.height());

    // 缩放图片
    let resized = img.resize(width, height, imageops::FilterType::Lanczos3);

    // 计算居中位置
    let x = (CANVAS_WIDTH - width) / 2;
    let y = (CANVAS_HEIGHT - height) / 2;

    // 将缩放后的图片绘制到画布上
    imageops::overlay(&mut canvas, &resized, x.into(), y.into());

    // 添加渐变层
    apply_gradient(&mut canvas);

    // =======================  添加水印： =======================
    // 在 process_image 函数中，在应用渐变效果之后 效果会更好
    // 加载字体
    let font_data = include_bytes!("Anto.ttf");
    let font = Font::try_from_bytes(font_data).ok_or("无法加载字体")?;

    // 设置文字属性
    // let text = "Hoodies";
    let text = shuiyin;
    // let scale = Scale::uniform(180.0); // 字体大小
    let scale = Scale::uniform(ziti_chicun); // 字体大小

    // 计算文字尺寸  这第一个版本 计算文字 尺寸和位置的话 如果文字尺寸很大 那么结果会很靠上
    // let v_metrics = font.v_metrics(scale);
    // let glyphs: Vec<_> = font
    //     .layout(text, scale, rusttype::Point { x: 0.0, y: 0.0 })
    //     .collect();
    // let text_width = glyphs
    //     .iter()
    //     .map(|g| g.position().x + g.unpositioned().h_metrics().advance_width)
    //     .last()
    //     .unwrap_or(0.0);
    // let text_height = v_metrics.ascent - v_metrics.descent;

    // // 计算居中位置
    // let x = ((CANVAS_WIDTH as f32 - text_width) / 2.0) as i32;
    // let y = ((CANVAS_HEIGHT as f32 - text_height) / 2.0) as i32;

    // 计算文字尺寸和  大小 v2   补偿了文字边界的偏移量  在布局时考虑了基线位置  考虑了文字的实际边界框
    // 计算文字尺寸
    // let v_metrics = font.v_metrics(scale);
    // let glyphs: Vec<_> = font
    //     .layout(
    //         text,
    //         scale,
    //         rusttype::Point {
    //             x: 0.0,
    //             y: v_metrics.ascent,
    //         },
    //     ) // 注意这里加上 ascent
    //     .collect();

    // // 获取文字边界
    // let glyphs_bounds = glyphs
    //     .iter()
    //     .filter_map(|g| g.pixel_bounding_box())
    //     .fold(None, |acc: Option<(i32, i32, i32, i32)>, bbox| match acc {
    //         None => Some((bbox.min.x, bbox.min.y, bbox.max.x, bbox.max.y)),
    //         Some((x1, y1, x2, y2)) => Some((
    //             x1.min(bbox.min.x),
    //             y1.min(bbox.min.y),
    //             x2.max(bbox.max.x),
    //             y2.max(bbox.max.y),
    //         )),
    //     })
    //     .unwrap_or((0, 0, 0, 0));

    // // 计算实际文字尺寸
    // let text_width = (glyphs_bounds.2 - glyphs_bounds.0) as f32;
    // let text_height = (glyphs_bounds.3 - glyphs_bounds.1) as f32;

    // // 计算居中位置
    // let x = ((CANVAS_WIDTH as f32 - text_width) / 2.0 - glyphs_bounds.0 as f32) as i32;
    // let y = ((CANVAS_HEIGHT as f32 - text_height) / 2.0 - glyphs_bounds.1 as f32) as i32;
    // 好像还是偏上
    // y=y-200

    // v3 第三种方式 计算文字尺寸
    // 设置文字属性
    // let text = "Hoodies";
    // let scale = Scale::uniform(180.0); // 字体大小

    // 计算文字尺寸和度量
    let v_metrics = font.v_metrics(scale);

    // 创建初始布局（使用临时位置）
    let glyphs: Vec<_> = font
        .layout(text, scale, rusttype::Point { x: 0.0, y: 0.0 })
        .collect();

    // 计算文字的边界框
    let bounds = glyphs
        .iter()
        .filter_map(|g| g.pixel_bounding_box())
        .fold(None, |acc: Option<(i32, i32, i32, i32)>, bbox| match acc {
            None => Some((bbox.min.x, bbox.min.y, bbox.max.x, bbox.max.y)),
            Some((x1, y1, x2, y2)) => Some((
                x1.min(bbox.min.x),
                y1.min(bbox.min.y),
                x2.max(bbox.max.x),
                y2.max(bbox.max.y),
            )),
        })
        .unwrap_or((0, 0, 0, 0));

    // 计算实际尺寸
    let text_width = (bounds.2 - bounds.0) as f32;
    let text_height = (bounds.3 - bounds.1) as f32;

    // 计算居中位置
    let x = ((CANVAS_WIDTH as f32 - text_width) / 2.0) as i32 - bounds.0;
    let y = ((CANVAS_HEIGHT as f32 - text_height) / 2.0) as i32 - bounds.1;

    // 绘制文字   这第一种  方块感觉很重
    // for glyph in glyphs {
    //     if let Some(bounding_box) = glyph.pixel_bounding_box() {
    //         glyph.draw(|gx, gy, intensity| {
    //             let gx = gx as i32 + bounding_box.min.x + x;
    //             let gy = gy as i32 + bounding_box.min.y + y;

    //             if gx >= 0 && gx < CANVAS_WIDTH as i32 && gy >= 0 && gy < CANVAS_HEIGHT as i32 {
    //                 let pixel = canvas.get_pixel_mut(gx as u32, gy as u32);
    //                 // 设置 透明度为28%
    //                 *pixel = Rgba([0, 0, 0, ((intensity * 255.0 * 0.28) as u8)]);
    //             }
    //         });
    //     }
    // }

    // 替换原来的绘制文字部分
    for glyph in font.layout(
        text,
        scale,
        rusttype::Point {
            x: x as f32,
            y: y as f32,
        },
    ) {
        if let Some(bounding_box) = glyph.pixel_bounding_box() {
            // glyph.draw(|gx, gy, intensity| {
            //     let gx = gx as i32 + bounding_box.min.x;
            //     let gy = gy as i32 + bounding_box.min.y;

            //     if gx >= 0 && gx < CANVAS_WIDTH as i32 && gy >= 0 && gy < CANVAS_HEIGHT as i32 {
            //         let pixel = canvas.get_pixel_mut(gx as u32, gy as u32);
            //         // 使用 f32 进行颜色计算以获得更平滑的效果
            //         let alpha = (intensity * 255.0 * 0.28) as u8;
            //         *pixel = Rgba([0, 0, 0, alpha]);
            //     }
            // });

            // 更精细的 alpha 混合版本  黑色版本
            // glyph.draw(|gx, gy, intensity| {
            //     let gx = gx as i32 + bounding_box.min.x;
            //     let gy = gy as i32 + bounding_box.min.y;

            //     if gx >= 0 && gx < CANVAS_WIDTH as i32 && gy >= 0 && gy < CANVAS_HEIGHT as i32 {
            //         let pixel = canvas.get_pixel_mut(gx as u32, gy as u32);
            //         let alpha = (intensity * 255.0 * 0.28) as u8;

            //         // 使用 alpha 混合
            //         let orig = pixel.0;
            //         let new_alpha = alpha as f32 / 255.0;
            //         *pixel = Rgba([
            //             ((1.0 - new_alpha) * orig[0] as f32) as u8,
            //             ((1.0 - new_alpha) * orig[1] as f32) as u8,
            //             ((1.0 - new_alpha) * orig[2] as f32) as u8,
            //             255,
            //         ]);
            //     }
            // });
            // 白色版本
            glyph.draw(|gx, gy, intensity| {
                let gx = gx as i32 + bounding_box.min.x;
                let gy = gy as i32 + bounding_box.min.y;

                if gx >= 0 && gx < CANVAS_WIDTH as i32 && gy >= 0 && gy < CANVAS_HEIGHT as i32 {
                    let pixel = canvas.get_pixel_mut(gx as u32, gy as u32);
                    let alpha = (intensity * 255.0 * 0.28) as u8;

                    // 使用 alpha 混合
                    let orig = pixel.0;
                    let new_alpha = alpha as f32 / 255.0;
                    *pixel = Rgba([
                        ((1.0 - new_alpha) * orig[0] as f32 + new_alpha * 255.0) as u8, // 白色 R=255
                        ((1.0 - new_alpha) * orig[1] as f32 + new_alpha * 255.0) as u8, // 白色 G=255
                        ((1.0 - new_alpha) * orig[2] as f32 + new_alpha * 255.0) as u8, // 白色 B=255
                        255,
                    ]);
                }
            });
        }
    }

    // =======================

    // 添加渐变层
    // apply_gradient(&mut canvas);

    // 保存结果
    let file_name = input_path
        .file_stem()
        .and_then(|s| s.to_str())
        .ok_or("无法获取文件名")?;

    let output_path = Path::new(output_dir).join(format!("{}.png", file_name)); // 图片保存

    canvas
        .save(output_path)
        .map_err(|e| format!("无法保存图片: {}", e))?;

    Ok(())
}

// 计算等比例缩放尺寸
fn calculate_dimensions(original_width: u32, original_height: u32) -> (u32, u32) {
    let target_height = CANVAS_HEIGHT;
    let ratio = original_width as f32 / original_height as f32;
    let new_width = (target_height as f32 * ratio) as u32;

    if new_width <= CANVAS_WIDTH {
        (new_width, target_height)
    } else {
        let target_width = CANVAS_WIDTH;
        let new_height = (target_width as f32 / ratio) as u32;
        (target_width, new_height)
    }
}

// 应用渐变效果
fn apply_gradient(canvas: &mut RgbaImage) {
    for y in 0..CANVAS_HEIGHT {
        for x in 0..CANVAS_WIDTH {
            // 计算渐变进度 (左下到右上)
            let progress = (x as f32 / CANVAS_WIDTH as f32
                + (CANVAS_HEIGHT - y) as f32 / CANVAS_HEIGHT as f32)
                / 2.0;

            // 计算渐变颜色
            let gradient_color = interpolate_color(&GRADIENT_START, &GRADIENT_END, progress);

            // 获取原始像素
            let pixel = canvas.get_pixel(x, y);

            // 应用正片叠底混合
            let new_pixel = multiply_blend(pixel, &gradient_color);

            // 更新像素
            canvas.put_pixel(x, y, new_pixel);
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

// 正片叠底混合模式
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

// 获取目录中的所有图片文件
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
