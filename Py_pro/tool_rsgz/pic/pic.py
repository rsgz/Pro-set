import subprocess,os
from PIL import Image, ImageDraw,ImageEnhance
import math
from PIL import ImageGrab
from PIL import Image, ImageDraw, ImageFont

class Pic:
    def __init__(self):
        pass

    # 等比例缩放 设置高度
    def set_gaodu_from_ffmpeg_dengbili(self,pic_path,h,save_path):
        r"""等比例缩放 设置高度"""
        command = [
            'ffmpeg',
            '-i', pic_path,  # 输入文件
            '-vf', f"scale=-1:{h}",  # 修改高度，保持宽高比
            '-q:v', '2',  # 设置输出质量
            '-y',
            save_path  # 输出文件

        ]
        # os.remove(pic_path)
        subprocess.run(command, check=True)


# 转换成base64
def convert_image_to_base64(image_path):
    # 以二进制模式读取 PNG 图像
    with open(image_path, "rb") as image_file:
        # 将图片编码为 base64
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    # 构建 JSON 对象
    result = {
        "filename": image_path.split(os.sep)[-1],  # 获取文件名（不包含路径）
        "base64Data": f"data:image/png;base64,{encoded_string}"  # 格式化 base64 字符串
    }
    # return json.dumps(result, indent=4)  # 返回格式化后的 JSON 数据
    return result

def create_gradient(width, height, start_color, end_color):
    """创建渐变色"""
    gradient = Image.new('RGBA', (width, height), color=0)
    draw = ImageDraw.Draw(gradient)

    for y in range(height):
        # 计算渐变颜色
        ratio = y / height
        r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
        g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
        b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)

        # 绘制渐变线条
        draw.line((0, y, width, y), fill=(r, g, b, 255))

    return gradient


def multiply_blend(image1, image2):
    """手动实现正片叠底效果"""
    # 确保两张图片都是RGBA模式
    image1 = image1.convert("RGBA")
    image2 = image2.convert("RGBA")

    # 获取图片数据
    pixels1 = np.array(image1)
    pixels2 = np.array(image2)

    # 正片叠底操作
    # 乘法并对255取余
    result_pixels = np.clip(pixels1[:, :, :3] * pixels2[:, :, :3] / 255, 0, 255).astype(np.uint8)

    # 添加Alpha通道
    result_pixels = np.dstack((result_pixels, pixels2[:, :, 3]))

    # 返回新的图片
    return Image.fromarray(result_pixels)

def Multiply(img_1, img_2):    # 确保两个图像都是"RGB"模式，并且大小相同
    # img_1 = img_1.convert("RGB")
    # img_2 = img_2.convert("RGB")

    # 创建一个新的空白图像，用于存放结果
    result = Image.new("RGB", img_1.size)

    # 获取两个图像的像素数据
    pixels_1 = img_1.load()
    pixels_2 = img_2.load()
    pixels_result = result.load()

    # 对每个像素应用正片叠底效果
    for x in range(img_1.width):
        for y in range(img_1.height):
            r1, g1, b1 = pixels_1[x, y]
            r2, g2, b2 = pixels_2[x, y]

            # 计算新的像素值
            new_r = int(r1 * r2 / 255)
            new_g = int(g1 * g2 / 255)
            new_b = int(b1 * b2 / 255)

            # 限制像素值在0-255之间
            new_r = min(255, max(0, new_r))
            new_g = min(255, max(0, new_g))
            new_b = min(255, max(0, new_b))

            # 设置结果图像的像素值
            pixels_result[x, y] = (new_r, new_g, new_b)

    # 保存结果图像
    # result.save(save)
    return result

# 正片叠底
def pil_zheng_pian_die_di(im_pil1,im_pil2):
    # img_1 = Image.open(p2)
    # img_2 = Image.open(p1)
    return Multiply(im_pil1,im_pil2)

# 粘贴板图片 存储到本地
def zhantieban_pic_save(save_pic_name):
    image = ImageGrab.grabclipboard()
    if isinstance(image, Image.Image):
        image.save(save_pic_name)
        print("图像已保存为 clipboard_image.png")
    else:
        print("剪贴板中没有图像")

# 获取粘贴板图片
def get_zhantieban_pic():
    image = ImageGrab.grabclipboard()
    if isinstance(image, Image.Image):
        return image
    else:
        print("剪贴板中没有图像")
        return 0

# 默认载入图片
def o(im1):
    return Image.open(im1)

# rgb模式载入
def o_rgb(im1):
    return Image.open(im1).convert('RGB')

# 有透明度通道
def o_rgba(im1):
    return Image.open(im1).convert('RGBA')

# 灰度模式
def o_l(im1):
    return Image.open(im1).convert('L')

# 返回图片的格式
def geshi(im1):
    return o(im1).format




# 获取文字尺寸
def get_font_render_size(text,font,fontsize):
    canvas = Image.new('RGB', (2048, 2048))
    draw = ImageDraw.Draw(canvas)
    monospace = ImageFont.truetype(font, fontsize)
    white = (255, 255, 255)
    draw.text((0, 0), text, font=monospace, fill=white)
    bbox = canvas.getbbox()
    # 宽高
    size = (bbox[2] - bbox[0], bbox[3] - bbox[1])
    return size

# pil_img图片添加文字
def add_wenzi(pil_img,font_path,font_size,text,color):
    # 加载图片
    # image_path = 'path_to_your_image.jpg'  # 替换为你的图片路径
    # image = Image.open(image_path)
    # 加载字体
    # font_path = 'path_to_your_font.ttf'  # 替换为你的字体文件路径
    # font_size = 40  # 设置字体大小
    text_width, text_height = get_font_render_size(text, font_path, font_size)
    font = ImageFont.truetype(font_path, font_size)
    # 要绘制的文字
    # text = "居中文字"
    # 使用ImageDraw创建一个可以在图片上绘制文字的对象
    draw = ImageDraw.Draw(pil_img)
    # text_width, text_height = draw.getsize(text, font=font)  # 计算文字尺寸
    # text_width, text_height = font.getsize(text)
    # 宽高
    print(text_width, text_height)
    x = (pil_img.width - text_width) / 2  # 计算文字位置
    y = (pil_img.height - text_height) / 2
    draw.text((x, y), text, font=font, fill=color)  # 假设文字颜色为白色
    return pil_img
    # 保存或显示图片
    # image.show()


# pil_img图片添加文字 能控制透明度
def add_wenzi2(pil_img,font_path,font_size,text,color,opacity):
    # 创建一个和目标图片一样大小的画布
    text_canvas = Image.new('RGBA', pil_img.size, (255, 255, 255, 0))
    text_width, text_height = get_font_render_size(text, font_path, font_size)
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(text_canvas) # 创建一个可以在画布上绘制的对象
    x = (pil_img.width - text_width) / 2  # 计算文字位置
    y = (pil_img.height - text_height) / 2
    # draw.text(text_position, text, font=font, fill=(255, 255, 255, 128))  # 在画布上绘制文字
    draw.text((x, y), text, font=font, fill=color)  # 假设文字颜色为白色
    alpha = text_canvas.split()[3]  # 获取画布的alpha通道
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)  # 0.5表示50%的透明度  # 调整alpha通道的透明度
    text_canvas.putalpha(alpha)  # 将调整后的alpha通道放回画布
    combined_img = Image.alpha_composite(pil_img.convert('RGBA'), text_canvas)  # 将带有文字的画布粘贴到目标图片上

    # # 保存或显示合成后的图片
    # combined_img.save('output_with_text.png')
    # combined_img.show()
    return combined_img

# 正片叠底2
def Multiply(img_1, img_2, save):
    img = (img_2/255.0)*(img_1/250.0)
    io.imsave(save, img)

# 创建透明图片
def creat_touming_pic(size):
    return Image.new('RGBA', size, (0, 0, 0, 0)) # 创建一个新的 RGBA 图像
    # image.save('transparent.png')  # 保存图片到本地文件

# 创建白底图片
def creat_baidi_pic(size):
    return Image.new('RGBA', size, (255, 255, 255, 255)) # 创建一个新的 RGBA 图像

# 白底大图 贴 小图
def baididatu_tie_xiaotu(size,im1,position):
    r"""
    :param size: 模板尺寸
    :param im1: 图片路径
    :param position: 图片位置
    :return:
    """
    # 大图 白底
    bg_img=creat_baidi_pic(size=size)
    img1 = Image.open(im1).convert('RGBA')
    # position1=(0,0)
    bg_img.paste(img1, position, img1)
    # bg_img.show()
    return bg_img

# 大的透明图 贴 小图
def datouming_tie_xiaotu(size,im1,position):
    r"""
    :param size: 模板尺寸
    :param im1: 图片路径
    :param position: 图片位置
    :return:
    """
    # 大图默认透明的
    bg_img=creat_touming_pic(size=size)
    img1 = Image.open(im1).convert('RGBA')
    # position1=(0,0)
    bg_img.paste(img1, position, img1)
    # bg_img.show()
    return bg_img

# 大图贴小图
def da_tie_xiaotu(bg_img,im1,position):
    r"""
    :param bg_img: 大图的PIL对象
    :param im1: 小图路径
    :param position: 小图位置
    :return:
    """
    # 大图默认透明的
    img1 = Image.open(im1).convert('RGBA')
    # position1=(0,0)
    bg_img.paste(img1, position, img1)
    # bg_img.show()
    return bg_img

# 每张图片的长度
def chang(im1):
    return Image.open(im1).convert('RGBA').size[0]

# 每张图片的高度
def gao(im1):
    return Image.open(im1).convert('RGBA').size[1]

# 计算总长度的平均 贴图x 是多少
def x_some(zong_x,xiaotu_l=[]):
    small_n = len(xiaotu_l)  # 小图个数
    small_all_len = sum([chang(small_pic) for small_pic in xiaotu_l])  # 小图的总宽
    shengyu_chang=  zong_x - small_all_len
    pingjun_jianxi = int(shengyu_chang/(small_n+1))
    return pingjun_jianxi

# 总的所有图片长度总和
def x_all(xiaotu_l=[]):
    small_all_len = sum([chang(small_pic) for small_pic in xiaotu_l])  # 小图的总宽
    return small_all_len

# 图片尺寸 缩放
def suofang_pic(img_pil,w,h):
    return img_pil.resize((w,h), Image.Resampling.LANCZOS)

if __name__ == '__main__':
    pass