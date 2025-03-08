import os
from PIL import Image

# 定义图片文件夹路径
# image_folder = r"E:\pic\leimu\Hoodies"
# image_folder = r"E:\pic\leimu\T-Shirts"
# image_folder = r"E:\pic\leimu\Hoodies"
# image_folder = r"E:\pic\leimu\Jackets"
# image_folder = r"E:\pic\leimu\Jeans"
# image_folder = r"E:\pic\leimu\Maxi Dresses"
# image_folder = r"E:\pic\leimu\Mini Dresses"
# image_folder = r"E:\pic\leimu\Pants"
# image_folder = r"E:\pic\leimu\Skirt"
# image_folder = r"E:\pic\leimu\Sweater"
image_folder = r"E:\pic\shangpin"

# 遍历文件夹中的所有图片
for filename in os.listdir(image_folder):
    # 获取文件的完整路径
    file_path = os.path.join(image_folder, filename)

    # 确保是文件而不是文件夹
    if os.path.isfile(file_path):
        try:
            # 打开图片
            with Image.open(file_path) as img:
                # 获取图片尺寸
                size = img.size
                # 创建子目录名称，格式为 "宽度x高度"
                size_folder = os.path.join(image_folder, f"{size[0]}x{size[1]}")

                # 如果子目录不存在，则创建
                if not os.path.exists(size_folder):
                    os.makedirs(size_folder)
                img.close()  # 显式关闭文件句柄
                # 移动图片到对应的子目录
                new_file_path = os.path.join(size_folder, filename)
                os.rename(file_path, new_file_path)

        except Exception as e:
            print(f"无法处理文件 {filename}: {e}")

print("图片分类完成！")