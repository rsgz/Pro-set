import os,shutil
list_mulu = os.listdir
j=os.path.join
cd=os.chdir
shanchu_kong_mulu=os.rmdir
shanchu_mulu=shutil.rmtree
shanchu_wenjian=os.remove
shiwenjian = os.path.isfile
shimulu = os.path.isdir
shifoucunzai = os.path.exists
xinjian_mulu = os.mkdir
xinjian_mulus = os.makedirs
fuzhi_mulu = shutil.copytree
fuzhi_wenjian = shutil.copyfile
chongmingming = os.rename
dangqianlujing=os.getcwd
dangqianwenjian=os.path.abspath(__file__)
fumulu = os.path.dirname
yidongwenjian=shutil.move
wenjianming=os.path.basename

mowei = lambda path: os.path.split(path)[-1]

def houzhuiming(wenjian_path):
    return os.path.splitext(wenjian_path)[-1]

def del_pic(mulu):
    mu_l = list_mulu_yiceng(mulu)
    for mu in mu_l:
        if "800x800" not in mowei(mu) and "600x800" not in mowei(mu) and "533x800" not in mowei(mu) and shimulu(mu):
            zi = j(mulu,mu)
            print(f"删除了 {zi}")
            shanchu_mulu(zi)

# 获取一层目录 目录列表
def list_mulu_yiceng(mulu):
    cd(mulu)
    mulu_l = list_mulu(".")
    mulu_set = [j(mulu,m) for m in mulu_l]
    return mulu_set

#
def print_l(mulu_set):
    print(*mulu_set, sep="\n")

mulu=r"E:\pic\leimu"
mulu_set = list_mulu_yiceng(mulu)
# print_l(mulu_set)
for mulu in mulu_set:
    del_pic(mulu)