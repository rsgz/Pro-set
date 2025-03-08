import os
from tool_rsgz.mulu.mulu import Mulu
from tool_rsgz.str.str import Str





class File:
    def __init__(self):
        self.p = Mulu()
        self.string=Str()
        pass

    # 获取所有文件
    def get_all_file(self,path):
        r"""获取所有文件"""
        f_l=[]
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                # f=p.hebing_path(dirpath, filename)
                # f_l.append(f)
                f_l.append(self.p.hebing_path(dirpath, filename))
        return f_l

    # 打印所有文件
    def print_all_file(self,path):
        r"""打印所有文件"""
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                print(self.p.hebing_path((dirpath,filename)))


if __name__ == '__main__':
    f=File()
    s = Str()
    p=Mulu()
    fl = f.get_all_file(r"E:\0-up1220-1")
    # f.print_all_file(r"E:\0-up1220-1")
    # print(*fl,sep="\n")
    # s.prints(fl)
    # print(p.yuanma_path())  #D:\0-code\tool_rsgz\mulu\path.py
    print("源码路径", p.yuanma_path())  # D:\0-code\tool_rsgz\file\file.py
    print("源码路径 base", p.yuanma_base_path())
    print("工作路径", p.work_dir())
    print("切换工作路径")
    p.cd(r"D:\58-anaconda")
    print("工作路径", p.work_dir())

