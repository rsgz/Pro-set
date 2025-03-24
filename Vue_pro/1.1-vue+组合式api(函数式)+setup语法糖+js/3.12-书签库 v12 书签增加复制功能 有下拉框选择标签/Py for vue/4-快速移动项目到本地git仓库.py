import os
import shutil





def copy_directory(src, dst, exclude_dirs):
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isdir(src_path):
            if item in exclude_dirs:
                print(f"跳过目录: {src_path}")
            else:
                shutil.copytree(src_path, dst_path)
        else:
            shutil.copy2(src_path, dst_path)



# 公司
# lao=r"E:\0-pro\rust_pro"
# lao=r"E:\0-pro\vue_pro"
# 公司
# xin = r"E:\0-git-data\Pro-set\Vue_pro\1.1-vue+组合式api(函数式)+setup语法糖+js\3.10-书签库 v9 vue+rust 改动了一点"


# 房间
# 房间
# lao = r"C:\Users\Administrator\Desktop\vue_pro"
# lao = r"C:\Users\Administrator\Desktop\rust_pro"
lao = r"C:\Users\Administrator\Desktop\Py for vue"
xin = r"F:\0-git-pro\Pro-set\Vue_pro\1.1-vue+组合式api(函数式)+setup语法糖+js\3.12-书签库 v12 书签增加复制功能 有下拉框选择标签"

m=lao.split(os.sep)[-1]
xin=os.path.join(xin,m)
print(m)

src_dir = lao
dst_dir = xin
exclude_dirs = {'target','node_modules','.git'}  # 要排除的目录名

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

copy_directory(src_dir, dst_dir, exclude_dirs)