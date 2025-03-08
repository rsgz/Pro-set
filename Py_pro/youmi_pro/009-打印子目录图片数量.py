import os
from pathlib import Path
from collections import defaultdict

# 指定父目录
p = r"E:/pic/shangpin"
parent_dir = Path(p)

# 用于存储子目录及其图片数量的字典
image_counts = defaultdict(int)

# 支持的图片格式
image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp','.webp'}

# 遍历父目录下的所有子目录
for subdir in parent_dir.iterdir():
    if subdir.is_dir():
        # 统计子目录中的图片数量
        image_count = 0
        for file in subdir.iterdir():
            if file.is_file() and file.suffix.lower() in image_extensions:
                image_count += 1
        # 将子目录名称和图片数量存入字典
        image_counts[subdir.name] = image_count

# 按图片数量降序排序
sorted_counts = sorted(image_counts.items(), key=lambda x: x[1], reverse=True)

# 打印结果
jilu = 0
for subdir, count in sorted_counts:
    if jilu>10:
        break
    s=f"子目录: {p}/{subdir}, 图片数量: {count}"
    print(s.replace("/","\\"))
    jilu=jilu+1